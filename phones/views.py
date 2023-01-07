from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by:
        sorts = {
            'name': Phone.objects.order_by('name'),
            'min_price': Phone.objects.order_by('price'),
            'max_price': reversed(Phone.objects.order_by('price'))
        }
        phones = sorts[request.GET.get('sort')]

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    ph = request.path[8:-1]
    phone = Phone.objects.get(slug=f'{request.path[9:-1]}')
    context = {'phone': phone}
    return render(request, template, context)
