from django.contrib import admin
from .models import Product, Message, Order, Order_Update, Review

# Register your models here.

admin.site.site_header = "Jalaram Collection Admin Panel"
admin.site.site_title = "Admin Panel"

admin.site.register((Product, Message, Order, Order_Update, Review))