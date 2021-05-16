from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name'] 


class ProfileForm(forms.ModelForm):
    PRbio = SummernoteTextField()
    class Meta:
        model = Profile
        fields = ['PRbio']