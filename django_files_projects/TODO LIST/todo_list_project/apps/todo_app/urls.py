from django.urls import path
from . import views

urlpatters=[
    path('homepage',views.ListingTasks.as_view(),name='homepage'),
    path('in_details_/<int:pk>/',views.DetailedTask.as_view(),name='detailed_task'),
    path('update_task/<int:pk>/',views.UpdateTask.as_view(),name='updated_task'),
    path('create_task/<int:pk>/',views.CreateTask.as_view(),name='created_task'),
    path('delete_task/<int:pk>/',views.DeleteTask.as_view(),name='deleted_task'),
    
]