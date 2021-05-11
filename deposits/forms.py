from django import forms
from deposits import models


class DepositForm(forms.ModelForm):
    class Meta:
        model = models.Deposit
        fields = [
            'deposit',
            'term',
            'rate',
            'interest',
        ]


class DepositFormNew(forms.ModelForm):
    class Meta:
        model = models.Deposit
        fields = [
            'deposit',
            'term',
            'rate',
        ]

    def save(self, commit=True):
        form_data = self.cleaned_data
        self.instance.interest = form_data['deposit'] * pow((1 + form_data['rate']), form_data['term']) - form_data['deposit']
        return super(DepositFormNew, self).save(commit)