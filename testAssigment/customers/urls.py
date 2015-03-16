from django.conf.urls import patterns, include, url
from customers.views import CustomerList
from customers.views import CreateCustomerView
from . import views

urlpatterns = patterns('',
    url(r'^$', CustomerList.as_view(), name="customer-list"),
    url(r'^create-customer$', CreateCustomerView.as_view(), name="create-customer"),
)
