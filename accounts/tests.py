from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()

class UserTest(TestCase):

    def setUp(self):
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_active = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)  
        self.assertNotEqual(user_count, 0)  

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password(self.user_a_pw))#check_password is belt in method that check if the password i entered is the same


    def test_login_url(self):
        #login_url = settings.LOGIN_URL 
        data = {'username': 'cfe', 'password': self.user_a}
        response = self.client.post('/login/', data, follow=True)
        #print(dir(response))
        status_code = response.status_code
        #print(response.request)
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, '/ar/login/' )
        self.assertEqual(status_code, 200)

