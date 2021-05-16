from django.db import models
from django.contrib.auth.models import User
from address.models import Shop
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.



User._meta.get_field('email')._unique = True




class Profile(models.Model):
    PRuser = models.OneToOneField(User, related_name='user_profile', verbose_name=_("user"), on_delete=models.CASCADE)
    PRbio = models.TextField(max_length=1000, verbose_name=_("Bio"))
    PRjoin_date = models.DateTimeField(default=datetime.datetime.now, verbose_name=_("join date"))
    PRslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))
    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def save(self, *args, **kwargs):
        if not self.PRslug:
            self.PRslug = slugify(self.PRuser.username)
        super(Profile, self).save(*args, **kwargs)        

    def __str__(self):
        return '%s' %(self.PRuser)

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"slug": self.PRslug})

    def get_shop_count(self):
        return Shop.objects.filter(SHcreated_by__exact=self.PRuser).count()    

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(PRuser=kwargs['instance'])

    post_save.connect(create_profile, sender= User) 