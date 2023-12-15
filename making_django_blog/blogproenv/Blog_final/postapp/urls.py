from django.urls import path,include
from .views import( Index,
                   ScienceRelated,
                   InDetails,
                   DeleteArticle,
                   CompleteDelete,
                   AddArticle,
                   EditArticle,
                   )

urlpatterns=[
    path('tinymce/',include('tinymce.urls')),
    path('',Index.as_view(),name='index'),
    path('post/<str:pk>/',InDetails.as_view(),name='details'),
    path('sciences/',ScienceRelated.as_view(),name='sciences'),
    path('<str:pk>/delete/',DeleteArticle.as_view(),name='delete_article'),
    path('compeletely_deleted/',CompleteDelete.as_view(),name='compeletely_deleted'),
    path('addnew_article/<str:pk>/',AddArticle.as_view(),name='addnew_article'),
    path('edit_an_article/<str:pk>/',EditArticle.as_view(),name='edit_article'),


    
 
]