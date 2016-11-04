from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from {{cookiecutter.app_name}}.users.views import UserViewSet, home

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = ([
    url(r'^$', home),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('authentication.urls')),
    url(r'^api/', include(router.urls)),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    # url(r'^rest/$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

]     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      + [url(r'^.*$', home)])
