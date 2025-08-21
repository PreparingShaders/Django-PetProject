from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='week_days_index'),
    path('<str:day>/', views.get_info_week_days, name='day_info')
]