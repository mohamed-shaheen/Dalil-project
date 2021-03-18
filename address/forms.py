from django import forms
from django.contrib.gis import forms as geoforms
from django.utils.translation import ugettext_lazy as _
from .models import Shop, Product



class NewShopForm(geoforms.ModelForm):
    
    SHlocation = geoforms.PointField(widget=geoforms.OSMWidget(
        attrs={'map_width': 600, 'map_height': 400, 'default_lon' : 31.233334, 'default_lat' : 30.033333, 'default_zoom' : 8 }), label=_("Map location")) 

    class Meta:
        model = Shop     
        fields = ["SHname", "SHgover", "SHaddress", "SHnum", "SHlocation"]


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["PRname", "PRcategory", "PRdesc", "PRref", "PRref_img" ]



