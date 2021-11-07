from django.test import TestCase
from address.models import Shop, Type
from django.contrib.auth.models import User
from django.utils.translation import activate
# Create your tests here.


class ShopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        #must change defult lang in settings.py to 'en' before runing the test
        activate('en')
        user = User.objects.create_user(username='mohamed', email='example@email.com',  password='testpass')
        type=Type.objects.create(TYname='type', TYdesc='some desc')
        shop = Shop.objects.create(SHname='the shop', SHtype=type, SHgover='QENA', SHaddress='some address', SHlocation='SRID=4326;POINT (31.026788 30.378931)', SHcreated_by=user)

    def test_SHname_label(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('SHname').verbose_name
        self.assertEqual(field_label, 'Naming the place')

    def test_SHtype_label(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('SHtype').verbose_name
        self.assertEqual(field_label, 'Place Type')

    def test_SHname_max_length(self):
        shop = Shop.objects.get(id=1)
        max_length = shop._meta.get_field('SHname').max_length
        self.assertEqual(max_length, 50)


    def test_get_absolute_url(self):
        shop = Shop.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(shop.get_absolute_url(), '/en/places/1-the-shop/')   