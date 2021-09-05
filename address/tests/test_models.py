from django.test import TestCase, testcases
from address.models import Shop
# Create your tests here.


class ShopModelTest(testcases):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Shop.objects.create(SHname='the shop', SHtype=1  )

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
        self.assertEqual(author.get_absolute_url(), 'places/1-the-shop')    