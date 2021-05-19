from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('PRuser',) 
    search_fields = ['PRuser__username']
    summernote_fields = ('PRbio',)


#admin.site.register(Profile)