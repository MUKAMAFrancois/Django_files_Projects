from django.urls import path
from book.views import post_search
from . import views
#
urlpatterns=[
    path('',views.post_search, name='search'),
]