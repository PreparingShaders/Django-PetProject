from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import  render_to_string
import calendar

signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dates = {
    ('capricorn', (12, 22), (1, 19)),
    ('aquarius', (1, 20), (2, 18)),
    ('pisces', (2, 19), (3, 20)),
    ('aries', (3, 21), (4, 19)),
    ('taurus', (4, 20), (5, 20)),
    ('gemini', (5, 21), (6, 20)),
    ('cancer', (6, 21), (7, 22)),
    ('leo', (7, 23), (8, 22)),
    ('virgo', (8,23), (9, 22)),
    ('libra', (9, 23), (10, 22)),
    ('scorpio', (10, 23), (11, 21)),
    ('sagittarius', (11, 22), (12, 21))
}

def get_yyyy_converters(request, sing_zodiac):
    return HttpResponse(f'Вы передали число из 4х чисел - {sing_zodiac}')

def get_my_float_converters(request, sing_zodiac):
    return HttpResponse(f'Вы передали вещественное число- {sing_zodiac}')


def get_my_date_converters(request, sing_zodiac):
    return HttpResponse(f'Вы передали год- {sing_zodiac}')

def get_my_split_converters(request, sing_zodiac):
    return HttpResponse(f'Возвращаем список строк- {sing_zodiac}')

def get_my_upper_converters(request, sing_zodiac):
    return HttpResponse(f'Возвращаем строку с изменением регистра- {sing_zodiac}')


def index(request):
    zodiacs = list(signs)
    li_elements = ''
    for sing in zodiacs:
        redirect_url = reverse('horoscope-name', args=[sing])
        li_elements += f'<li> <a href="{redirect_url}">{sing.title()} </a> </li>'
    response = f'''
    <ol>
        {li_elements}
    </ol>
    '''
    return HttpResponse(response)


# Create your views here.
def get_info(request, sing_zodiac: str):
    return render(request, 'horoscope/index.html')

def get_info_number(request, sing_zodiac: int):
    zodiacs = list(signs)
    if sing_zodiac > len(zodiacs):
        return HttpResponse(f'Неправильный порядковый номер знака зодиака - {sing_zodiac}')
    name_zodiac = zodiacs[sing_zodiac - 1]
    redirect_urls = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_urls)
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)


def type_index(request):
    li_elements = ''
    for type in types_dict:
        li_elements += f'<li> <a href = "{type}/"> {type.title()} </a> </li>'
    return HttpResponse(f'<ol> {li_elements} </ol>')

def type(request, type_name):
    li_elements = ''
    for sing in types_dict[type_name]:
        redirect_path = reverse('horoscope-name', args=[sing])
        li_elements += f'<li> <a href= "{redirect_path}"> {sing.title()} </a> </li>'
    return  HttpResponse(f'<ol> {li_elements} </ol>')

def horoscope_by_date(request, month, day):
    if month < 1 or month > 12:
        return HttpResponse('Неверный месяц')
    if day < 1 or day > calendar.monthrange(2025, month)[1]:
        return HttpResponse('Неверный день для этого месяца')

    for sign, (start_month, start_day), (end_month, end_day) in zodiac_dates:
        if (start_month == end_month and start_day <= day <= end_day and month == start_month) or \
                (start_month < end_month and (
                        (month == start_month and day >= start_day) or (month == end_month and day <= end_day))) or \
                (start_month > end_month and (
                        (month == start_month and day >= start_day) or (month == end_month and day <= end_day))):
            return HttpResponse(f"Знак зодиака: {sign.title()}")

    return HttpResponse("Неверная дата")