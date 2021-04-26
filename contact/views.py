from django.shortcuts import render, redirect
from .models import Contact
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
