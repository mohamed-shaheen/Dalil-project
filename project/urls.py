"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_email_verification import urls as email_urls
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('address.urls' , namespace='address')),
    path('', include('accounts.urls' , namespace='accounts')),
    path('', include('contact.urls' , namespace='contact')),
    path('avatar/', include('avatar.urls')),
    path('email/', include(email_urls)),
    path('summernote/', include('django_summernote.urls')),
    path('404/', TemplateView.as_view(template_name="404.html")),
    path('403/', TemplateView.as_view(template_name="403.html")),
    path('500/', TemplateView.as_view(template_name="500.html")),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
