from deposits import models, forms
from django.views.generic import View, ListView, FormView, DetailView
from django.urls import reverse_lazy


# Create your views here.
class DepositsView(ListView):
    model = models.Deposit
    template_name = 'deposit_list.html'


class DepositDetailView(DetailView):
    model = models.Deposit
    template_name = 'deposit_detail.html'


class AddDepositView(FormView):
    form_class = forms.DepositFormNew
    template_name = 'deposit_add.html'
    success_url = reverse_lazy('deposit-list')

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        return response
