from django.urls import path
from . import views

app_name = 'address'


urlpatterns = [
    path('', views.home_view, name='home'  ),
    path('products/', views.all_products, name='product_list'),
    path('shops/', views.all_shops, name='shops_list'),
    path('shops/<int:id>/<slug:slug>/', views.shop_detail, name='shop_detail')
]