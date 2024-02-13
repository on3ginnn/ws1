from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    catalog = Catalog.objects.all()
    return render(request,template_name="index.html" ,context = {"catalog" : catalog})


def category(request, catalog_id):
    catalog = Catalog.objects.all()
    catalog_prod = Catalog.objects.get(id=catalog_id)
    product = Products.objects.filter(catalog=catalog_prod)

    return render(request, template_name="category.html", context = {"catalog" : catalog, 'category':catalog_prod.title, "product" : product})

