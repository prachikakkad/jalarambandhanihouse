from django.urls import path
from .import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('/', views.Home),
    path('shop', views.Shop_Home),
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
    path('getotp', views.Get_OTP, name="getotp"),
    path('paying-options', views.Paying_Options, name="paying-options"),
    path('paying-option-selected', views.Payment_Proceed, name="pay_proceed"),
    path('verifying' , views.Verifying, name="verifying"),
]