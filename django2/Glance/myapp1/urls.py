from django.urls import path
from . import views
from .views import(
    Display
)
# urls

#app_name='myapp1'

urlpatterns=[
   path('',Display.as_view()),
   path('register/', views.register, name='register'),
   path('login/', views.login, name='login'),
   path('logout/',views.logout,name='logout'),
   path('detail/<str:pk>',views.detailView, name='detail'), # dynamic url, just detail view
   path('listing/', views.listing, name='listing'), # list view
 
]
