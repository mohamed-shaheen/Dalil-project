from django.shortcuts import render, redirect, get_object_or_404
from .models import About
from django.utils.translation import get_language_bidi
from django.contrib.auth.models import User
from .forms import ContactForm
# Create your views here.




def contact_us(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            mail = request.POST['COemail']
            user = User.objects.filter(email__exact=mail).exists()
            if user:
                contact.COis_user = True
            contact.save()    

            return redirect('address:home')
    else:
        form = ContactForm()

    context = {'form':form}
    return render(request, 'contact_form.html', context )   


def about_us(request):
    if get_language_bidi():
        abouts = get_object_or_404(About, ABon_page=True, ABis_arabic=True)
    else :    
        abouts =  get_object_or_404(About, ABon_page=True, ABis_arabic=False)

    context = {'abouts' : abouts}
    return render(request, 'about_us.html', context)
