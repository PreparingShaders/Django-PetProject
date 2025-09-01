from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.SplitConverter, 'my_split')
register_converter(converters.UpperConvertor, 'my_upper')


urlpatterns = [
    path('', views.index, name='horoscope-name'),
    path('<int:sign_zodiac>/', views.get_info_number),
    path('<str:sign_zodiac>/', views.get_info, name='horoscope-name'),
]