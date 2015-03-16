from django.conf.urls import patterns, include, url
from customers.views import CustomerList
from . import views

urlpatterns = patterns('',
    url(r'^$', CustomerList.as_view(), name="customer-list"),
)
