from django.shortcuts import render
from customers.models import Customer
from django.views.generic.list import ListView

class CustomerList(ListView):

    model = Customer
