from django.contrib import admin
from .models import Shop, Customer, Advertisement, Follow, HashTag, ShopCategory
# Register your models here.
admin.site.register(Shop)
admin.site.register(Customer)
admin.site.register(Advertisement)
admin.site.register(Follow)
admin.site.register(HashTag)
admin.site.register(ShopCategory)
