from django.urls import path
from . import views

urlpatterns=[
    path('',views.cart_details,name='cart_detail'),
    path('add_product/<int:product_id>/',views.cart_add,name='cart_add'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    
]