from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Count
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_views(request):
    template = 'books/catalog.html'
    data = Book.objects.all()
    context = {'books': data, }
    return render(request, template, context)


def book(request, date):
    template = 'books/catalog.html'
    dates = sorted([book[0].strftime('%Y-%m-%d') for book in Book.objects.values_list('pub_date').distinct('pub_date')])
    try:
        nextd = dates[dates.index(date) + 1]
    except IndexError:
        nextd = None
    try:
        if dates.index(date) == 0:
            previosd = None
        else:
            previosd = dates[dates.index(date) - 1]
    except IndexError:
        previosd = None

    data = Book.objects.filter(pub_date=date)
    context = {'books': data,
               'nextd': nextd,
               'previosd': previosd,
               }
    return render(request, template, context)
