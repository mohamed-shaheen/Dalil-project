from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django_summernote.widgets import SummernoteWidget


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput(), label=_("E-mail"))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name'] 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['PRbio']
        widgets = {'PRbio': SummernoteWidget(attrs={
            'summernote':{
                'toolbar': [
                    ['style', ['style']],
                    ['font', ['bold', 'underline', 'clear']],
                    ['fontname', ['fontname']],
                    ['color', ['color']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['table', ['table']],
                    ['insert', ['link',]],
                    ['view', ['fullscreen', 'codeview', 'help']],
                ],
            }
        })}