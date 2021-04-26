from django import forms
from leaflet.forms.widgets import LeafletWidget
from django.utils.translation import ugettext_lazy as _
from .models import Shop, Product


class MapWidget(LeafletWidget):
    geometry_field_class = 'SHlocation'
class NewShopForm(forms.ModelForm):
    
    class Meta:
        model = Shop     
        fields = ["SHname", "SHtype", "SHgover", "SHaddress", "SHnum", "SHlocation"]
        widgets = {'SHlocation': MapWidget()}


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["PRname", "PRcategory", "PRdesc", "PRref", "PRref_img" ]



