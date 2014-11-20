from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView

from .models import Greeting
# Create your views here.

class WAH_Test(APIView):

    def post(self, request):
        return HttpResponse("/got it/")

    def index(self, request):

        return HttpResponse('WeAreHere placeholder.')


    def db(self, request):

        greeting = Greeting()
        greeting.save()

        greetings = Greeting.objects.all()

        return render(request, 'db.html', {'greetings': greetings})
