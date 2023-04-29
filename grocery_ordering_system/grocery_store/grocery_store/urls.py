"""grocery_store URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/',views.Master,name ='master'),
    path('',views.Index,name ='index'),
    path('signup',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),


    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


    path('contact_us',views.contact_page,name='contact_page'),
    path('details',views.details,name='details'),

    path('checkout/',views.CheckOut,name='checkout'),
    path('order/', views.Your_Order, name='order'),
    path('blog/', views.Blog, name='blog'),
    path('product/',views.Product_page,name='product'),
    path('product/<str:id>',views.Product_Detail,name='product_detail'),
    path('search/', views.Search, name='search'),
    

    
    path('seller/',views.seller,name='seller_page'),
    path('products_list/',views.products_list,name='products_list'),
    path('products_delete/<int:pk>/',views.products_delete,name='products_delete'),
    path('products_edit/<int:pk>/',views.products_edit,name='products_edit'),
    # path('products_delete/<int:pk>/', views.product_delete, name='dashboard-products-delete'),
    path('orders_list/',views.orders_list,name='orders_list'),
    path('admin_register/',views.admin_register,name='admin_register'),
    path('admin_login/',views.admin_login,name='admin_login'), 
   
    # path('seller/',views.seller,name='seller_page'),







] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

