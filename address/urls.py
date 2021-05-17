from django.urls import path
from . import views

app_name = 'address'


urlpatterns = [
    path('', views.home_view, name='home'  ),
    path('products/', views.all_products, name='product_list'),
    path('places/', views.all_shops, name='place_list'),
    path('places/<int:id>/<slug:slug>/', views.shop_detail, name='place_detail'),
    path('places/product/<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
    path('places/add', views.add_shop, name= 'add_place'),
    path('places/<int:id>/product/add', views.add_product, name= 'add_product'),
    path('places/<int:id>/<slug:slug>/edit/', views.ShopUpdateViews.as_view(), name='edit_place'),
    path('places/product/<int:id>/<slug:slug>/edit', views.ProductUpdateViews.as_view(), name='edit_product')
]