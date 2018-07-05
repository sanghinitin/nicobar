from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as rest_framework_views


urlpatterns = [
    url(r'^register', views.UserCreate.as_view(), name='account-create'),
    url(r'^details', views.UserDetail.as_view(), name='account-details'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]