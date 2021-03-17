from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop, Product, GOVERNORATES_CHOICES
from django.contrib.auth.decorators import login_required
from .forms import NewShopForm
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
        if pro_name and gov_name!='Choose...':
            products = products.filter(PRname__icontains=pro_name).filter(PRshop__SHgover__exact=gov_name)
        elif pro_name:
            products = products.filter(PRname__icontains=pro_name)
        else:
            products = products.filter(PRshop__SHgover__exact=gov_name)

    context = {'products' : products, 'govs' : GOVERNORATES_CHOICES}
    return render(request, 'products/product_list.html', context)   


def all_shops(request):
    shops = Shop.objects.all()

    if 'shop-bar' in request.GET:
        shop_name = request.GET['shop-bar']
        gov_name = request.GET['gover-bar']
        if shop_name and gov_name!='Choose...':
            shops = shops.filter(SHname__icontains=shop_name).filter(SHgover__exact=gov_name)
        elif shop_name:
            shops = shops.filter(SHname__icontains=shop_name)
        else:
            shops = shops.filter(SHgover__exact=gov_name)

    context = {'shops' : shops, 'govs' : GOVERNORATES_CHOICES}
    return render(request, 'shops/shop_list.html', context )

def shop_detail(request, id, slug):
    shop = get_object_or_404(Shop, pk=id, SHslug=slug)
    products = Product.objects.filter(PRshop__id__exact=id)
    if 'product-bar' in request.GET:
        pro_name = request.GET['product-bar']
        if pro_name:
            products = products.filter(PRname__icontains=pro_name)

    context = {'shop' : shop, 'products' : products}
    return render(request, 'shops/shop_detail.html', context)

@login_required
def add_shop(request):
    if request.method == "POST":
        form = NewShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.SHcreated_by = request.user
            shop.save()

            return redirect('address:shop_list')
    else:
        form = NewShopForm()

    context = {'form' : form}
    return render(request,'shops/shop_add.html', context)     
