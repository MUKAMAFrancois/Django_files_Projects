from django.urls import path
from . import views

# create urlpatterns

urlpatterns=[
    path('',views.index,name='index'),
]