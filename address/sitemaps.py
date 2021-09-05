from django.contrib.sitemaps import Sitemap
from .models import Shop, Product



class ShopSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    protocol = 'https'
    i18n = True

    def items(self):
        return Shop.objects.all()

    def lastmod(self, obj):
        return obj.SHcreated_dt    

#    def location(self, item):
#        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    protocol = 'https'
    i18n = True

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.PRcreated_dt

