from django import forms
from leaflet.forms.widgets import LeafletWidget
from django.utils.translation import ugettext_lazy as _
from .models import Shop, Product
#from django.contrib.gis.geos import Point

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
        fields = ["PRname", "PRcategory", "PRprice", "PRdesc", "PRref", "PRref_img" ]


#class ShopAdminForm(forms.ModelForm):
#
#    '''
#      this form for show lat and lon in admin panel just for view not editing
#    '''
#
#    latitude = forms.FloatField(
#        min_value=-90,
#        max_value=90,
#        required=True,
#    )
#    longitude = forms.FloatField(
#        min_value=-180,
#        max_value=180,
#        required=True,
#    )
#
#    class Meta(object):
#        model = Shop
#        exclude = []
#        widgets = {'point': forms.HiddenInput()}
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        coordinates = self.initial.get('SHlocation', None)
#        if isinstance(coordinates, Point):
#            self.initial['longitude'], self.initial['latitude'] = coordinates.tuple
#           
#
#    def clean(self):
#        data = super().clean()
#        latitude = data.get('latitude')
#        longitude = data.get('longitude')
#        point = data.get('SHlocation')
#        if latitude and longitude and not point:
#            data['point'] = Point(longitude, latitude)
#        return data
