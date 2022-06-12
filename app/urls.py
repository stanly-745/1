from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('worker/<str:pk>/',views.worker,name='worker'),
    path('addcustomer/',views.customerform,name='addcus'),
    path('addworker/',views.workerform,name='addwor'),
    path('addstock/',views.stockform,name='addsto'),
    path('addorder/',views.orderform,name='addord'),
    path('addproduct/',views.productform,name='addpro'),
    path('order',views.order,name='order'),
    path('order_history',views.order_history,name='order-his'),
    path('update-order/<str:pk>/',views.update_order,name='up-order'),
    path('stockin',views.stock,name='stock'),
    path('products',views.product,name='product'),
    path('update-stock/<str:pk>/',views.update_stock,name='up-stock'),

]