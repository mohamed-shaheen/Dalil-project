from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.



User._meta.get_field('email')._unique = True




class Profile(models.Model):
    PRuser = models.OneToOneField(User, related_name='user_profile', verbose_name=_("user"), on_delete=models.CASCADE)
    PRbio = models.CharField(max_length=100, verbose_name=_("Address"))
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
        return reverse("accounts:profile", kwargs={"id" : self.pk,"slug": self.PRslug})

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(PRuser=kwargs['instance'])

    post_save.connect(create_profile, sender= User) 