from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
# Create your models here.




GOVERNORATES_CHOICES = [
    ('ALEX', _('Alexandria')),
    ('ASW', _('Aswan')),
    ('ASYT', _('Asyut')),
    ('BEHA', _('Beheira')),
    ('BEF', _('Beni Suef')),
    ('CAI', _('Cairo')),
    ('DAKA', _('Dakahlia')),
    ('DAMA', _('Damietta')),
    ('FAI', _('Faiyum')),
    ('GHA', _('Gharbia')),
    ('GIZ', _('Giza')),
    ('ISM', _('Ismailia')),
    ('KAFH', _('Kafr El Sheikh')),
    ('LUX', _('Luxor')),
    ('MATH', _('Matruh')),
    ('MINA', _('Minya')),
    ('MONF', _('Monufia')),
    ('NEWY', _('New Valley')),
    ('NOSI', _('North Sinai')),
    ('POSA', _('Port Said')),
    ('QALA', _('Qalyubia')),
    ('QENA', _('Qena')),
    ('REDS', _('Red Sea')),
    ('SHAQ', _('Sharqia')),
    ('SOHG', _('Sohag')),
    ('SOSI', _('South Sinai')),
    ('SUZE', _('Suez')),

]

class Shop(models.Model):

    SHname = models.CharField(max_length=50, verbose_name=_("Shop name"))
    SHgover = models.CharField(max_length=50, choices=GOVERNORATES_CHOICES, verbose_name=_("Governorate"))
    SHaddress = models.TextField(max_length=300, verbose_name=_("Detailed address"))
    SHlocation = models.PointField(verbose_name=_("Map location"))
    SHslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))

    
    def save(self, *args, **kwargs):
        if not self.SHslug :
           self.SHslug = slugify(self.SHname )
        super(Shop, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")

    #def get_absolute_url(self):
    #    return reverse("", kwargs={"slug": self.SHslug})

    def __str__(self):
        return self.SHname

