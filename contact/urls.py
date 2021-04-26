from django.urls import path
from . import views

app_name = 'contact'


urlpatterns = [
    path('contact-us/', views.contact_us, name='contact_us'),
]