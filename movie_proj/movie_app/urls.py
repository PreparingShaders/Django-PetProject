from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug>', views.show_one_movie, name= 'movie-detail'),
]
