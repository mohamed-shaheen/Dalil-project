from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Shop, Product, Category, Type
from import_export.admin import ImportExportModelAdmin
#from .forms import ShopAdminForm
# Register your models here.

admin.site.site_header = 'Dalil Admin Panel'
admin.site.site_title = 'Dalil Admin Panel'

@admin.register(Shop)
class ShopAdmin(LeafletGeoAdmin, ImportExportModelAdmin):
    #form = ShopAdminForm
    display_raw = True
    list_display = ('SHname', 'SHtype', 'SHgover', 'SHaddress', 'SHlocation', 'SHcreated_dt') 
    list_filter = ('SHtype__TYname', 'SHgover')
    search_fields = ['SHname', 'SHcreated_by__username']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('CAname', 'CAdesc') 
    search_fields = ['CAname']

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('PRname', 'PRshop', 'PRdesc', 'PRcategory', 'PRcreated_dt') 
    list_filter = ('PRcategory__CAname', 'PRshop__SHgover', 'PRshop__SHtype__TYname')
    search_fields = ['PRname', 'PRshop__SHname', 'PRshop__SHcreated_by__username']



@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin):
    list_display = ('TYname', 'TYdesc')
    search_fields = ['TYname'] 
