from django.test import TestCase
from django.urls import reverse
from address import views
from django.contrib.auth import get_user_model
from address.models import Shop,Type
from django.contrib.gis.geos import Point
# Create your tests here.

class HomeTest(TestCase):

    #def create_whatever(self, title="only a test", body="yes, this is only a test"):
    #    return Whatever.objects.create(title=title, body=body, created_at=timezone.now())
    
    
    def test_home_view(self):
           # w = self.create_whatever()
            url = reverse("address:home")
            resp = self.client.get(url)

            self.assertEqual(resp.status_code, 200)
            #self.assertIn(w.title, resp.content)


User = get_user_model()

class ProductUpdateTest(TestCase):
   
    
    def setUp(self):
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'user_2@invalid.com', 'user_password')
        self.user_b = user_b
        type=Type.objects.create(TYname='type', TYdesc='some desc')
        shop_a = Shop.objects.create(SHname='shop a', SHtype=type, SHgover='QENA', SHaddress='some address', SHlocation='SRID=4326;POINT (31.026788 30.378931)', SHcreated_by=user_a)
        shop_b = Shop.objects.create(SHname='shop b', SHtype=type, SHgover='QENA', SHaddress='some address', SHlocation=Point(31.026788, 30.378931), SHcreated_by=user_b)
        self.shop_a = shop_a
        self.shop_b = shop_b


    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_shop_count(self):
        shop_count = Shop.objects.all().count()
        self.assertEqual(shop_count, 2)    

    def test_permission_denied_request(self):
        self.client.login(username=self.user_b, password='user_password')
        shop_1 = Shop.objects.get(SHname='shop a').get_absolute_url()
        shop_2 = Shop.objects.get(SHname='shop b').get_absolute_url()
        #print(shop_2)
        response_1 = self.client.post(shop_1+"edit/", {"SHaddress":"the address update"})
        response_2 = self.client.post(shop_2+"edit/", {"SHaddress":"the address update"})
        self.assertEqual(response_1.status_code, 403) 
        self.assertEqual(response_2.status_code, 200)

    def test_superuser_permission_request(self):
        self.client.login(username=self.user_a, password=self.user_a_pw)
        shop_1 = Shop.objects.get(SHname='shop a').get_absolute_url()
        shop_2 = Shop.objects.get(SHname='shop b').get_absolute_url()
        #print(shop_2)
        response_1 = self.client.post(shop_1+"edit/", {"SHaddress":"the address update for super"})
        response_2 = self.client.post(shop_2+"edit/", {"SHaddress":"the address update for super"})
        self.assertEqual(response_1.status_code, 200) 
        self.assertEqual(response_2.status_code, 200)