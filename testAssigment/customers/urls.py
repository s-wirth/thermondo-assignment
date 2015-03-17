from django.conf.urls import patterns, include, url
from customers.views import CustomerList, CreateCustomerView, CustomerUpdateView
from . import views

urlpatterns = patterns('',
    url(r'^$', CustomerList.as_view(), name="customer-list"),
    url(r'^create-customer$', CreateCustomerView.as_view(), name="create-customer"),
    url(r'^customer-update/(?P<pk>\d+)$', CustomerUpdateView.as_view(), name="customer-update"),
    # url(r'^send-email$', EmailView.as_view(), name="send-email"),
    url(r'^send-email/(?P<pk>\d+)$', 'customers.views.mail', name="send-email"),
)
