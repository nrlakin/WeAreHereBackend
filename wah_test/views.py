from django.shortcuts import render
from django.http import HttpResponse, HttpResponseDirect
import requests

from .models import Greeting
# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponseDirect('/hello/')

    else:
        return HttpResponse('WeAreHere placeholder.')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
