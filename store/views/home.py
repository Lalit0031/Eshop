from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.category import Category
from store.models.product import Product
from django.views import View


def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryids(categoryID)

    else:
        products = Product.get_all_products()

    data = {}
    data["products"] = products
    data["categories"] = categories

    print(products)
    print(categories)

    return render(request, 'index.html', data)


def About(request):
    return render(request, 'about.html')