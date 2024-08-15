from django.contrib import admin
from .models import (
    Vendor,
    ProductCategory,
    Product,
    Order,
    OrderItems,
    CustomerAddress,
    ProductRating,
)

# Register your models here.
admin.site.register(Vendor)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(CustomerAddress)
admin.site.register(ProductRating)
