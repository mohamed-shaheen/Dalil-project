from django.shortcuts import render
from .models import Shop, Product, GOVERNORATES_CHOICES
# Create your views here.


def home_view(request):
    shops=Shop.objects.all()
    context={'shops' : shops, 'govs' : GOVERNORATES_CHOICES}
    return render(request, 'shops/home.html', context)


def all_products(request):
    products = Product.objects.all()

    if 'product-bar' in request.GET:
        pro_name = request.GET['product-bar']
        gov_name = request.GET['gover-bar']
        print(gov_name)
        if pro_name and gov_name!='Choose...':
            products = products.filter(PRname__icontains=pro_name).filter(PRshop__SHgover__exact=gov_name)
        elif pro_name:
            products = products.filter(PRname__icontains=pro_name)
        else:
            products = products.filter(PRshop__SHgover__exact=gov_name)

    context = {'products' : products}
    return render(request, 'products/product_list.html', context)    