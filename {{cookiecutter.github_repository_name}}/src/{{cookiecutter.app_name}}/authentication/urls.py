from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import urls

from rest_framework.urlpatterns import format_suffix_patterns

from {{cookiecutter.app_name}}.authentication import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^logout/$', views.Logout.as_view()),
    url(r'^active-user/$', views.ActiveUser.as_view()),
    # url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
