from django.contrib import admin

from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "category", "price"]


class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]


class AdminCustomer(admin.ModelAdmin):
    list_display = ["first_name", "email", "phone"]


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
