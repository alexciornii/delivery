from django.contrib import admin
from .models import Provider
from .models import Consumer
from .models import Category
from .models import Product
from .models import Store
from .models import Order
from .models import OrderProduct


class ProviderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Provider, ProviderAdmin)


class ConsumerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Consumer, ConsumerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class StoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Store, StoreAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderProduct, OrderProductAdmin)
