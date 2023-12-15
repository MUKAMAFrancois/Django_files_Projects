from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import Listing_All
#from .feeds import LatestPostsFeed
#
urlpatterns=[
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),name='change_password'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/change_password_done.html'), name='password_change_done'),
   # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/',views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('signup/',views.signup, name='signup'),

      #Password Reset
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/passwords/enter_email_to_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/passwords/password_reset_done.html'),name='password_reset_done'),

  path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/passwords/enter_new_password_reset.html'),name='confirm_reset'),
  path('reset/finished/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/passwords/reset_complete.html'),name='reset_complete'),

   # path('feed/',LatestPostsFeed(),name='post_feed'),
  #  path('all',views.listing_all,name='all'),
    path('',Listing_All.as_view(),name='all'),
  #  path('tech',views.listing_tech, name='tech'),
  #  path('post/<str:slug>/',Detailing.as_view(),name='detail'),
    path('post/<str:slug>',views.detailing,name='detail'),
]