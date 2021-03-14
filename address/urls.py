from django.urls import path
from . import views

app_name = 'address'


urlpatterns = [
    path('', views.home_view, name='home'  ),
    path('product_list/', views.all_products, name='product_list'),
]