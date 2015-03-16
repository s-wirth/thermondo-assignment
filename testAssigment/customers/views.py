from django.shortcuts import render

def customer_list(request):
    return render(request, 'customers/customers.html', {})
