from customers.models import Customer
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
import smtplib

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

def mail(request, pk):
    customer = Customer.objects.get(id=pk)
    template = get_template('customers/email/email.html')
    context = Context({'customer': customer})
    content = template.render(context)
    email = EmailMessage('Hello', content, settings.EMAIL_HOST_USER,
            ['a.sophiewirth@gmail.com'])
    email.content_subtype = 'html'
    email.send(fail_silently=False)

    return HttpResponse('You send an email!')
