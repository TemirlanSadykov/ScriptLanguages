from django.shortcuts import render

from .models import Product

def front_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'front_page.html', context)