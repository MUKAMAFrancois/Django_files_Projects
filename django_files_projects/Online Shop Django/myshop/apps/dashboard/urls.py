from django.urls import path
from . import views


urlpatterns = [
      path('',views.listing_products, name='home_index'),
      path('all_laptops/',views.explore_laptops,name='all_laptops'),
      path('all_phones/',views.explore_phones,name='all_phones'),
      path('all_gadgets/',views.explore_gadgets,name='all_gadgets'),

      path('product_details/<str:id>/<slug:slug>/',views.product_detail,name='in_details'),
      

    
]