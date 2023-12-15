
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('apps.accounts.urls')),
    path('',include('apps.todos_app.urls')),
]
