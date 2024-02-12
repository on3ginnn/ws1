from django.shortcuts import render
from django.http import HttpResponse


def catalog_list(request):
    return render(request, "index.html", context={'li': 'li'})
    return HttpResponse('<body>Каталог<body>')