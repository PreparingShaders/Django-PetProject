from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from  django.urls import reverse

people = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
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
