from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

" When there is a request towards \products call this function"


# changes
def index(httprequest):
    products = Product.objects.all()

    return render(httprequest, 'index.html',
                  {'products': products})


def new_products(httprequest):
    return HttpResponse("New Products")
