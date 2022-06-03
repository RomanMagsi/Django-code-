from django.contrib import admin
from .Models.Product import Product
from .Models.Category import Category
from .Models.Customer import Customer
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
