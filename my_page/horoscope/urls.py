from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.type_index),
    path('type/<str:type_name>/', views.type, name='type_name'),
    path('<int:sing_zodiac>/', views.get_info_number),
    path('<str:sing_zodiac>/', views.get_info, name='horoscope-name'),
    path('<int:month>/<int:day>/', views.horoscope_by_date, name='horoscope_by_date')
]