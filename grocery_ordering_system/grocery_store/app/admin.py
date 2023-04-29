
from django.contrib import admin

# Register your models here.
from .models import Category, DetailsOfUser,Sub_Category,Product,contact_us,Order,Brand


admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(contact_us)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(DetailsOfUser)
