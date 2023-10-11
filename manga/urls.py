from django.urls import path
from . import views

urlpatterns = [
    path('manga/', views.MangaAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('manga/<int:id>/',
         views.MangaAPIViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('reviews/', views.ReviewAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('reviews/<int:id>/',
         views.ReviewAPIViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('genres/', views.GenreAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('genres/<int:id>/',
         views.GenreAPIViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
