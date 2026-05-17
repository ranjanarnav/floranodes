from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import re_path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tos/', views.tos, name='tos'),
    path('about/', views.about, name='about'),
    path('mc-plan/', views.mc, name='mc_plan'),
    path('vps/', views.vps, name='vps'),
    path('intel-xeon/', views.itl, name='intel-xeon'),
    path('amd-epyc/', views.amd, name='amd-epyc'),
    path('ryzen/', views.ryz, name='ryzen'),
    path('dc/', views.dc, name='dc'),
    path('privacy/', views.pp, name='privacy'),
    path('refund/', views.rp, name='refund'),
    path('usage/', views.up, name='usage'),
    path('contact/', views.contact_view, name='contact'),
]
# Use the full path to your app views here:
handler404 = 'shop.views.custom_404'
handler500 = 'shop.views.custom_500'
