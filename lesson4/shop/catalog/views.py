from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ProductForm
from .models import Product


def get_catalog(request):
    context = {'product_list': Product.objects.only('name', 'price')}
    return render(request, 'catalog/catalog.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Товар успешно добавлен!')
            return HttpResponseRedirect(reverse('catalog:catalog'))
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'catalog/product.html', context)
