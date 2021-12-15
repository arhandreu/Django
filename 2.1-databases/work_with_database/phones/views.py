from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    dict_sort = {'min_price': 'price',
                 'max_price': '-price',
                 'name': 'name',
    }
    if request.GET.get('sort', None):
        data = Phone.objects.order_by(dict_sort.get(request.GET.get('sort')))
    else:
        data = Phone.objects.all()
    context = {'phones': data}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    data = Phone.objects.get(slug=slug)
    context = {'phone': data}
    return render(request, template, context)
