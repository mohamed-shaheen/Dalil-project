from django import forms
from django.contrib.gis import forms as geoforms
from leaflet.forms.widgets import LeafletWidget
from django.utils.translation import ugettext_lazy as _
from .models import Shop, Product


class MapWidget(LeafletWidget):
    geometry_field_class = 'SHlocation'
class NewShopForm(forms.ModelForm):
    
    #SHlocation = geoforms.PointField(widget=geoforms.OSMWidget(
    #    attrs={'map_width': 600, 'map_height': 400, 'default_lon' : 31.233334, 'default_lat' : 30.033333, 'default_zoom' : 8 }), label=_("Map location")) 

    class Meta:
        model = Shop     
        fields = ["SHname", "SHtype", "SHgover", "SHaddress", "SHnum", "SHlocation"]
        widgets = {'SHlocation': MapWidget()}


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["PRname", "PRcategory", "PRdesc", "PRref", "PRref_img" ]



