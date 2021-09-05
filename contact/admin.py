from django.contrib import admin
from .models import Contact, About
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('COsubject', 'COtype', 'COemail', 'COis_seen', 'COin_progress', 'COis_user', 'COcreated_dt') 
    list_filter = ('COis_user', 'COtype', 'COis_seen', 'COin_progress')
    search_fields = ['COemail', 'COsubject', 'COmessage']


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('ABtitle', 'ABcreated_dt') 
    search_fields = ['ABtitle', 'ABcreated_dt']
    list_filter = ('ABon_page', 'ABis_arabic')
    summernote_fields = ('ABmain',)
