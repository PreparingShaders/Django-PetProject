from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from  django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'week_days/index.html')


def get_info_week_days(request, day: str):
    return render(request, 'week_days/day.html', {'day': day})