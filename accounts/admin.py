from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('PRuser', 'PRbio') 
    search_fields = ['PRuser__username']


#admin.site.register(Profile)