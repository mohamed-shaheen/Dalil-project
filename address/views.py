from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop, Product, Category, GOVERNORATES_CHOICES, Type
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.utils import timezone
from el_pagination.decorators import page_template
from .forms import NewShopForm, ProductForm
#from django.urls import reverse_lazy
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


    context = {'products' : products, 'category' : category, 'govs' : GOVERNORATES_CHOICES}
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)   

@page_template('shops/shop_list_page.html') 
def all_shops(request, template='shops/shop_list.html', extra_context=None):
    shops = Shop.objects.all()
    types = Type.objects.all()
    req = request.GET
    if ('q2' in req) and ('q3' in req) and ('q7' in req):
        shop_name = req['q3']
        gov_name = req['q2']
        shop_type = req['q7']
        shops = shops.filter(
            SHname__icontains=shop_name).filter(
                SHgover__icontains=gov_name).filter(
                    SHtype__TYname__icontains=shop_type)


    context = {'shops' : shops, 'govs' : GOVERNORATES_CHOICES, 'types' : types}
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context )

@page_template('shops/shop_list_product.html')
def shop_detail(request, id, slug, template='shops/shop_detail.html', extra_context=None):
    shop = get_object_or_404(Shop, pk=id, SHslug=slug)
    products = Product.objects.filter(PRshop__id__exact=id).order_by('PRname')
    if 'q1' in request.GET:
        pro_name = request.GET['q1']
        if pro_name:
            products = products.filter(PRname__icontains=pro_name)

    context = {'shop' : shop, 'products' : products}
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)


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


@method_decorator(login_required, name= 'dispatch')    
class ShopUpdateViews(UpdateView):
    model = Shop
    form_class = NewShopForm
    #fields = ('SHname', 'SHtype', 'SHgover', 'SHaddress', 'SHnum')
    template_name = 'shops/edit-shop.html'
    pk_url_kwarg = 'id'
    slug_url_kwarg = 'slug'
    slug_field = 'SHslug'
    query_pk_and_slug = True
    context_object_name = 'shop'  

    def form_valid(self, form):
        
            shop = form.save(commit=False)
            shop.SHupdated_by = self.request.user
            shop.SHupdated_dt = timezone.now()
            shop.save()     
            return redirect('address:place_detail', id=shop.pk, slug=shop.SHslug) 

    def dispatch(self, request, *args, **kwargs):
            # here you can make your custom validation for any particular use
            if ( self.get_object().SHcreated_by == request.user) or (request.user.is_superuser):
                pass
            else:    
                raise PermissionDenied()
            
            return super().dispatch(request, *args, **kwargs)     


@method_decorator(login_required, name= 'dispatch')
class ProductUpdateViews(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit-product.html'
    pk_url_kwarg = 'id'
    slug_url_kwarg = 'slug'
    slug_field = 'PRslug'
    query_pk_and_slug = True
    context_object_name = 'product'             


    def form_valid(self, form):
        
        product = form.save(commit=False)
        product.save()     
        return redirect('address:product_detail', id=product.pk, slug=product.PRslug) 

    def dispatch(self, request, *args, **kwargs):
            # here you can make your custom validation for any particular use
            if ( self.get_object().PRshop.SHcreated_by == request.user) or (request.user.is_superuser):
                pass
            else:    
                raise PermissionDenied()
            
            return super().dispatch(request, *args, **kwargs) 


@login_required
def shop_del(request, id):
    shop = get_object_or_404(Shop, pk=id)
    if (shop.SHcreated_by == request.user) or (request.user.is_superuser):
        shop.delete()
        return redirect('accounts:profile', slug=request.user.user_profile.PRslug)
    else:
        raise PermissionDenied()    


@login_required
def product_del(request, id):
    product = get_object_or_404(Product, pk=id)
    if (product.PRshop.SHcreated_by == request.user) or (request.user.is_superuser):
        product.delete()
        return redirect('address:place_detail', id=product.PRshop.pk, slug=product.PRshop.SHslug)
    else:
        raise PermissionDenied() 
