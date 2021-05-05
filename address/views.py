from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Shop, Product, Category, GOVERNORATES_CHOICES
from django.contrib.auth.decorators import login_required
from el_pagination.decorators import page_template
from .forms import NewShopForm, ProductForm
# Create your views here.


def home_view(request):
    category=Category.objects.all()
    context={'category' : category, 'govs' : GOVERNORATES_CHOICES}
    return render(request, 'shops/home.html', context)

@page_template('products/product_list_page.html')  
def all_products(request, template='products/product_list.html', extra_context=None):
    products = Product.objects.all().order_by('PRname')
    category = Category.objects.all()
    req = request.GET

    if 'q1' in req:
    
        if ('q1' in req) and ('q2' in req) and ('q3' in req) and ('q4' in req) and ('q5' in req) and ('q6' in req):
            pro_name = req['q1']
            gov_name = req['q2']
            shop_name = req['q3']
            adrs_name = req['q4']
            desc_name = req['q5']
            cate_name = req['q6']
            
            products = products.filter(
                PRname__icontains=pro_name).filter(
                    PRshop__SHgover__icontains=gov_name).filter(
                        PRshop__SHname__icontains=shop_name).filter(
                            PRshop__SHaddress__icontains=adrs_name).filter(
                                PRdesc__icontains=desc_name).filter(
                                    PRcategory__CAname__icontains=cate_name)
        elif ('q1' not in req) and ('q2' not in req) and ('q3' not in req) and ('q4' not in req) and ('q5' not in req) and ('q6' not in req) :

            return redirect('address:product_list')        


    context = {'products' : products, 'category' : category, 'govs' : GOVERNORATES_CHOICES}
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)   


def all_shops(request):
    shops = Shop.objects.all()

    if 'q3' in request.GET:
        shop_name = request.GET['q3']
        gov_name = request.GET['q2']
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
    if 'q1' in request.GET:
        pro_name = request.GET['q1']
        if pro_name:
            products = products.filter(PRname__icontains=pro_name)

    context = {'shop' : shop, 'products' : products}
    return render(request, 'shops/shop_detail.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, pk=id, PRslug=slug)

    context = {'product' : product}
    return render(request, 'products/product_detail.html', context)


@login_required
def add_shop(request):
    if request.method == "POST":
        form = NewShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.SHcreated_by = request.user
            shop.save()

            return redirect('address:place_list')
    else:
        form = NewShopForm()

    context = {'form' : form}
    return render(request,'shops/shop_add.html', context)     


@login_required
def add_product(request, id):
    shop = get_object_or_404(Shop, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.PRshop = shop
            product.save()

            return redirect('address:place_detail', id=shop.pk, slug=shop.SHslug)
    else:
        form = ProductForm()

    context = {'form' : form, 'shop' : shop}
    return render(request,'products/product_add.html', context) 


    


