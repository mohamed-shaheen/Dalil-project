from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Shop, Product, Category, Type
# Register your models here.

admin.site.site_header = 'Dalil Admin Panel'
admin.site.site_title = 'Dalil Admin Panel'

@admin.register(Shop)
class ShopAdmin(LeafletGeoAdmin):
    list_display = ('SHname', 'SHtype', 'SHgover', 'SHaddress', 'SHlocation') 
    list_filter = ('SHtype__TYname', 'SHgover')
    search_fields = ['SHname', 'SHcreated_by__username']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('CAname', 'CAdesc') 
    search_fields = ['CAname']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('PRname', 'PRshop', 'PRdesc', 'PRcategory') 
    list_filter = ('PRcategory__CAname', 'PRshop__SHgover', 'PRshop__SHtype__TYname')
    search_fields = ['PRname', 'PRshop__SHname', 'PRshop__SHcreated_by__username']



@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('TYname', 'TYdesc')
    search_fields = ['TYname'] 
