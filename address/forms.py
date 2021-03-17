from django.contrib.gis import forms
from django.utils.translation import ugettext_lazy as _
from .models import Shop



class NewShopForm(forms.Form):
    name = forms.CharField( )
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 600, 'map_height': 400, 'default_lon' : 31.233334, 'default_lat' : 30.033333 }))
