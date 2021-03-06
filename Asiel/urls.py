from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf.urls import url
from .views import *
admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
 
    path('Enviar_correo/', EnviarEmail.as_view() ,name='enviar'),


    # urls django_registration
    path('accounts/', include('registration.backends.default.urls')),
    
    # urls django_comments_xtd 
    path(r'^comments/', include('django_comments_xtd.urls')),

    # urls django-newsletter
    path(r'^newsletter/', include('newsletter.urls')),
    
    # urls djangocms-blog 
    path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]


urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    url(r"^django-check-seo/", include("django_check_seo.urls")), 
    path("", include("cms.urls")))


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
