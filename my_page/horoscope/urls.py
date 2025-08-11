from django.urls import path
from . import views

urlpatterns = [
    path('<int:sing_zodiac>/', views.get_info_number),
    path('<str:sing_zodiac>/', views.get_info)
]