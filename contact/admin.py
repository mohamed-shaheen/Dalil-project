from django.contrib import admin
from .models import Contact
# Register your models here.



@admin.register(Contact)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('COsubject', 'COtype', 'COemail', 'COis_seen', 'COin_progress', 'COis_user') 
    list_filter = ('COis_user', 'COtype', 'COis_seen', 'COin_progress')
    search_fields = ['COemail', 'COsubject', 'COmessage']