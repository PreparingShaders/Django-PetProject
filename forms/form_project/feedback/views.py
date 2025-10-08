from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForms

# Create your views here.
def index(request):
    form = FeedbackForms()
    if  request.method == 'POST':
        form = FeedbackForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/done')
    form = FeedbackForms()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')
