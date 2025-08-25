from django.db.models import query
from django.shortcuts import HttpResponse, render
from store.models import Product


def say_hello(request): #learning how to retrieve data form db 2:36:58
    product = Product.objects.get(pk=1)
        
    return render(request, 'hello.html')