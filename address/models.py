from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator
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

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+201000000'. Up to 15 digits allowed.")

class Shop(models.Model):

    SHname = models.CharField(max_length=50, help_text=_("The name of your project, then choice type"), verbose_name=_("Naming the place"))
    SHtype = models.ForeignKey("Type", related_name="type_product", on_delete=models.CASCADE, verbose_name=_("Place Type"))
    SHgover = models.CharField(max_length=50, choices=GOVERNORATES_CHOICES, verbose_name=_("Governorate"))
    SHaddress = models.CharField(max_length=300, verbose_name=_("Detailed address"))
    SHnum = models.CharField(validators=[phone_regex], max_length=15,null= True, blank=True, verbose_name=_("Phone number"))
    SHlocation = models.PointField(verbose_name=_("Map location"))
    SHcreated_dt = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"))
    SHcreated_by = models.ForeignKey(User, related_name="user_shop", on_delete=models.CASCADE, verbose_name=_("Created by"))
    SHupdated_dt = models.DateTimeField(null=True, verbose_name=_("Updated date"))
    SHupdated_by = models.ForeignKey(User, null=True, blank=True, related_name="+", on_delete=models.CASCADE, verbose_name=_("Updated by"))
    SHslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))

    
    def save(self, *args, **kwargs):
        if not self.SHslug :
           self.SHslug = slugify(self.SHname )
        super(Shop, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")
    
    #@property
    #def  lat_lng(self):
    #    return list(getattr(self.SHlocation, 'coords', [])[::-1])   

    def get_absolute_url(self):
        return reverse("address:place_detail", kwargs={"id" : self.id, "slug": self.SHslug})

    def __str__(self):
        return self.SHname

    def get_product_count(self):
        return Product.objects.filter(PRshop=self).count()

class Type(models.Model):

    TYname = models.CharField(max_length=50, help_text="Ex: 'Market'or'Clinic' etc..", verbose_name=_("Type name"))
    TYdesc = models.TextField(max_length=400, verbose_name=_("Description"))
    TYref_img = models.URLField(max_length=500, null=True, verbose_name=_("Link image"))
    TYslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))
    

    def save(self, *args, **kwargs):
        if not self.TYslug :
            self.TYslug = slugify(self.TYname )
        super(Type, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self):
        return self.TYname


   


class Product(models.Model):
    
    PRname = models.CharField(max_length=50, verbose_name=_("Product name"))
    PRshop = models.ForeignKey(Shop, related_name="shop_product", on_delete=models.CASCADE, verbose_name=_("Name of place"))
    PRdesc = models.TextField(max_length=400, help_text=_("Write about the product quality and how the product work ^_^ .."), verbose_name=_("description"))
    PRref = models.URLField(max_length=400, null=True, blank=True, verbose_name=_("Outside reference link"))
    PRref_img = models.URLField(max_length=500, null=True, blank=True, verbose_name=_("Link image"))    
    PRcategory = models.ForeignKey("Category", related_name="category_product", on_delete=models.CASCADE, verbose_name=_("Category"))
    PRprice = models.DecimalField(max_digits=10, decimal_places=2,  validators=[MinValueValidator(0.1, message=_("Must be a postive number."))], blank= True, null=True, verbose_name=_("Price") )
    PRslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))


    def save(self, *args, **kwargs):
        if not self.PRslug :
           self.PRslug = slugify(self.PRname )
        super(Product, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")    

    def get_absolute_url(self):
        return reverse("address:product_detail", kwargs={"id" : self.id, "slug": self.PRslug})        

    def __str__(self):
        return self.PRname



class Category(models.Model):
    
    CAname = models.CharField(max_length=50, verbose_name=_("Category name"))
    CAdesc = models.TextField(max_length=400, verbose_name=_("Description"))
    CAref_img = models.URLField(max_length=500, null=True, verbose_name=_("Link image"))
    CAslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))


    def save(self, *args, **kwargs):
        if not self.CAslug :
           self.CAslug = slugify(self.CAname )
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")    

    #def get_absolute_url(self):
    #    return reverse("", kwargs={"slug": self.CAslug})        

    def __str__(self):
        return self.CAname

 
