from django.urls import path
from . import views

# create urlpatterns
app_name='blogapp'

urlpatterns=[
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register/',views.registration,name='register'),
    path('index/',views.index,name='index'),
    path('post/<str:pk>',views.readfull,name='fulltext'),
]