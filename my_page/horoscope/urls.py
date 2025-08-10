from django.urls import path
from . import views

urlpatterns = [
    path('<sing_zodiac>/', views.get_info)
]