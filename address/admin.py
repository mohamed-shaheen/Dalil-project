from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Product, Category
# Register your models here.


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('SHname', 'SHgover', 'SHaddress', 'SHlocation') 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('CAname', 'CAdesc') 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('PRname', 'PRdesc', 'PRcategory')       