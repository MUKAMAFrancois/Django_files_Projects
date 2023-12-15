
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.dashboard.urls')),
    #The namespace argument in Django urls is used to uniquely identify a set of URLs.
    path('cart/',include('apps.cart.urls')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)