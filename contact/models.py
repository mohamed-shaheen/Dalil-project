from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
#from django.urls import reverse
from django.utils.text import Truncator
# Create your models here.

TYPE_CHOICES = [
    ('COMT', _('Complaint')),
    ('SUGGS', _('Suggestions')),
    ('LINR', _('Links Error')),
    ('REPR', _('Report a user')),
    ('PROS', _('Property rights')),
    ('OTHS', _('Others')),
]

class Contact(models.Model):
    COemail = models.EmailField(verbose_name=_("E-mail"))
    COsubject = models.CharField(max_length=50, verbose_name=_("Subject"))
    COtype = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name=_("Message type") )
    COmessage = models.TextField(max_length=8000, help_text=_("Reports an error or user , copy > paste the 'link' or 'user name' "), verbose_name=_("Message") )
    COcreated_dt = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_("Created at"))
    COis_seen = models.BooleanField(default=False, verbose_name=_("Seen"))
    COin_progress = models.BooleanField(default=False, verbose_name=_("In progress"))
    COis_user = models.BooleanField(default=False, verbose_name=_("Is user"))
    COslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))


    def save(self, *args, **kwargs):
        if not self.COslug :
           self.COslug = slugify(self.COsubject )
        super(Contact, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    #def get_absolute_url(self):
    #    return reverse("address:place_detail", kwargs={"id" : self.id, "slug": self.COslug})

    def __str__(self):
        return self.COsubject   


class About(models.Model):
    ABtitle = models.CharField(max_length=100, verbose_name=_('Title'))
    ABmain = models.TextField(max_length=15000, verbose_name=_('Main'))
    ABcreated_dt = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    ABon_page = models.BooleanField(default=False, verbose_name=_("View as main"))


    class Meta:
        verbose_name = _("About")
        verbose_name = _("About")

    def __str__(self):
        truncted_message = Truncator(self.ABtitle)
        return truncted_message.chars(15)   
