from django.shortcuts import render
from customers.models import Customer
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from post_office import mail

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

class EmailView(TemplateView):

    model = Customer
    mail.send(
        'a.sophiewirth@gmail.com', # List of email addresses also accepted
        'your.generic.test.email@gmail.com',
        subject='My email',
        message='Hi there!',
        html_message='Hi <strong>there</strong>!',
    )
    template_name = 'customers/send_email.html'
