from django.shortcuts import render
from .models import Shop
# Create your views here.


def home_view(request):
    shops=Shop.objects.all()
    context={'shops' : shops}
    return render(request, 'shops/home.html', context)