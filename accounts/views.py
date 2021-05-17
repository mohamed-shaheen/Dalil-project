from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django_email_verification import send_email
from .models import Profile
from address.models import Shop
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

# Create your views here.




def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auth_login(request,user)
            user.is_active = False 
            send_email(user)
            return redirect('address:home')
    context = {'form':form}      

    return render(request,'signup.html', context)


def profile(request, slug):
    profile = get_object_or_404(Profile, PRslug=slug)
    shops = Shop.objects.filter(SHcreated_by__exact=profile.PRuser)


    context = {'profile' : profile, 'shops' : shops }
    return render(request, 'profile.html', context)

def re_send(request):
    if 'email' in request.POST:
        email = request.POST['email']
        try:
           user = User.objects.get(email=email)
        except User.DoesNotExist:
            error = 'This E-mail does not exist please try again :-)'
            context = {'error' : error}
            return render(request, 'email-confirm/confirm_template.html', context)
    if user.is_active:
        return redirect('address:home')
    else:
        send_email(user)
        return redirect('accounts:login')       


def profile_edit(request):
    profile = Profile.objects.get(PRuser=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.PRuser = request.user
            myprofile.save()
            return redirect('accounts:profile', slug=profile.PRslug)

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    context = {'userform':userform , 'profileform':profileform, 'profile':profile}  

    return render(request,'edit-profile.html', context)        