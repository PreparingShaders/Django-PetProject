from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from  django.urls import reverse

people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]

# Create your views here.
def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret SUPER MAN',
        'bar_name': 'Bob’s BBQ & Grill WORK',
        'count_needle': '8.8.8.8 IP RESOLVE DNS EQ',
    }
    return render(request, 'week_days/index.html', context=context)

def get_info_about_people(request):
    data = {
        'people': people
    }
    return render(request, 'week_days/people.html', context=data)

def get_info_about_name(request, name_post: str):
    data = {
        'name' : name_post
    }
    return render(request, 'week_days/detail_by_name.html', context=data)

def get_info_about_number(request, number_post:int):
    data = {
        'number' : number_post
    }
    return render(request, 'week_days/details_bu_number.html', context=data)
