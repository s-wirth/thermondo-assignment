from django.shortcuts import render
from customers.models import Customer
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

class CustomerList(ListView):

    model = Customer

class CreateCustomerView(CreateView):

    model = Customer
    template_name = 'customers/create_customer.html'

    def get_success_url(self):
        return reverse('customer-list')

class CustomerUpdateView(UpdateView):

    model = Customer
    template_name = 'customers/customer_update_form.html'

    def get_success_url(self):
        return reverse('customer-list')
