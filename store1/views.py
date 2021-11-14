from django.shortcuts import render, get_object_or_404
from store1.models import Product

from store1.models import ProductImage


def product_list(request):
    products = Product.objects.all()
    return render(request, "store1/products.html", {'products': products})


def product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    product_image = Product.objects.filter(pk=pk).prefetch_related('images').first()


    return render(request, 'store1/product.html', {'product': item, "image": product_image})

