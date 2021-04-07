from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.models import User
from django_email_verification import send_email
from .models import Profile
from address.models import Shop

# Create your views here.




def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            user.is_active = False 
            send_email(user)
            return redirect('address:home')
    context = {'form':form}      

    return render(request,'signup.html', context)


def profile(request, id, slug):
    profile = get_object_or_404(Profile, pk=id, PRslug=slug)
    shops = Shop.objects.filter(SHcreated_by__exact=request.user)


    context = {'profile' : profile, 'shops' : shops }
    return render(request, 'profile.html', context)