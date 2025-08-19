from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.SplitConverter, 'my_split')
register_converter(converters.UpperConvertor, 'my_upper')


urlpatterns = [
    path('', views.index),
    path('type/', views.type_index),
    path('<my_upper:sing_zodiac>/', views.get_my_upper_converters),
    path('<my_split:sing_zodiac>/', views.get_my_split_converters),
    path('<my_date:sing_zodiac>/', views.get_my_date_converters),
    path('type/<str:type_name>/', views.type, name='type_name'),
    path('<yyyy:sing_zodiac>/', views.get_yyyy_converters),
    path('<int:sing_zodiac>/', views.get_info_number),
    path('<my_float:sing_zodiac>/', views.get_my_float_converters),
    path('<str:sing_zodiac>/', views.get_info, name='horoscope-name'),
    path('<int:month>/<int:day>/', views.horoscope_by_date, name='horoscope_by_date')
]