"""Ecommerce_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from shop import views
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.Home, name="home"),
    path('admin/', admin.site.urls, name="admin"),
    path('contact', views.Contact, name="contact"),
    path('about', views.About, name="about"),
    path('login', views.Login, name="login"),
    path('signup', views.Signup, name="signup"),
    path('creating-account', views.Create_User,name="new_user"),
    path('logging-in', views.Log_In, name="Log_In"),
    path('logged-out', views.Log_Out, name="Log_Out"),
    path('profile', views.Profile, name="Profile"),
    path('contacting', views.Contacting, name="contacting"),
    path('product-<int:myid>', views.Product_View, name="product_view"),
    path('checkout', views.Checkout , name="checkout"),
    path('place-order', views.Place_Order , name="place_order"),
    path('thank', views.Thank_You, name="thank"),
    path('tracker', views.Tracker, name="tracker"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/favicon.ico'))),
    path('search' , views.Search, name="search"),
    path('review', views.review, name="review"),
    path('verify' , views.Verify, name="verify"),
    path('verifying' , views.Verifying, name="verifying"),
    path('getotp', views.Get_OTP, name="getotp"),
    path('paying-options', views.Paying_Options, name="paying-options"),
    path('paying-option-selected', views.Payment_Proceed, name="pay_proceed"),
    path('shop' , views.Shop_Home),
    path('shop/', include('shop.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)