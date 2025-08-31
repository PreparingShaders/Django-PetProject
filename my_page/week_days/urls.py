from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.get_guinness_world_records, name='test'),
    path('post/<str:name_post>', views.get_info_about_name, name='name_post'),
    path('post/<int:number_post>', views.get_info_about_number, name='number_post'),
    path('people/', views.get_info_about_people, name='people'),
]