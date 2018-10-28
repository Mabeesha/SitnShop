"""Advertiser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from .views import shop, market, customer

app_name = 'market'

urlpatterns = [
        path('', shop.IndexView.as_view(), name='homepage'),
        path('login/', market.LoginINAs, name='loginAs'),
        path('login/loginShop/', shop.loginShop, name="loginShop"),
        path('login/signupShop/', shop.signupShop, name="signupShop"),

        # path('login/loginShop/', shop.ShopLoginView.as_view(), name="loginShop"),


        # todo: create a federated login for shopvisitor
        path('login/signupCustomer/', customer.CustomerSignUpView.as_view(), name="signupCustomer"),
        path('login/loginCustomer/', customer.loginCustomer, name="loginCustomer"),


        path('edit_shop/', shop.create_addvertisement, name='edit_shop'),
        path('edit_customer/', customer.edit_customer, name='edit_customer'),

        path('profile/', market.Profile, name='profile'),
        path('logout/', market.LogOUT, name='logout'),
        path("public/<pk>/", market.public_profile, name="public_profile"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

