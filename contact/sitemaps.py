from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.8
    protocol = 'https'
    i18n = True

    def items(self):
        return ['contact:contact_us', 'contact:about_us', 'address:home']  

    def location(self, item):
        return reverse(item)
