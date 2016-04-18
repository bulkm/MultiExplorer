from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from views import home, register_new_wallet_user, login

urlpatterns = [
    url(r'^$', home, name="wallet"),
    url(r'^register_new_wallet_user', register_new_wallet_user, name="register_new_wallet_user"),
    url(r'^login', login, name='login'),
]
