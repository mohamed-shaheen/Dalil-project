from django.test import TestCase
from django.urls import reverse
from address import views
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