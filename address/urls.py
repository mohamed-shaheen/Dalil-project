from django.urls import path
from . import views

app_name = 'address'


urlpatterns = [
    path('', views.home_view, name='home'  ),
    path('products/', views.all_products, name='product_list'),
    path('shops/', views.all_shops, name='shop_list'),
    path('shops/<int:id>/<slug:slug>/', views.shop_detail, name='shop_detail'),
    path('shops/add', views.add_shop, name= 'add_shop'),
    path('shops/<int:id>/product/add', views.add_product, name= 'add_product'),
]