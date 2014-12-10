from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from django.http import Http404
from wah_test.models import CheckIn, Occupant
#from wah_test.serializers import CheckInSerializer, OccupantSerializer
from wah_test.serializers import *
from wah_test.forms import *
from knn_classifier import *
from wah_test.permissions import *

# Create your views here.
class Location(APIView):
    """
    Get location from beacon ranges.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        serializer = BeaconSerializer(data = request.DATA, many = True)
        if serializer.is_valid():
            location = KNNClassifier().get_room(serializer.data)
            return Response({'room_id':location})
        return Response(status = status.HTTP_204_NO_CONTENT)

class CheckInView(generics.ListCreateAPIView):
    """
    Check update room with checkin.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserList(generics.ListAPIView):
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserDetail(APIView):

    def get(self, request, format=None):

        if request.user == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class Occupancy(APIView):
    """
    Add new occupant or get list of current occupants.
    """
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        occupants = Occupant.objects.all()
        serializer = OccupantSerializer(occupants, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OccupantSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Update(APIView):
    """
    Update, retrieve, or delete a single user.
    """

    permission_classes = (IsUserOrReadOnly,)

    def get_occupant(self, id):
        try:
            return Occupant.objects.get(pk = id)
        except Occupant.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        occupant = self.get_occupant(id)
        serializer = OccupantSerializer(occupant, data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, id, format=None):
        occupant = self.get_occupant(id)
        serializer = OccupantSerializer(occupant)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        occupant = self.get_occupant(id)
        occupant.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

def register(request):
    """
    taken from tangowithdjango.com
    """
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        occ_form = OccupantForm(data=request.POST)

        if user_form.is_valid() and occ_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            occupant = occ_form.save(commit=False)
            occupant.user = user

            occupant.save()

            registered = True
        else:
            print user_form.errors, occ_form.errors
    else:
        user_form = UserForm()
        occ_form = OccupantForm()

    return render(request, 'wah_test/register.html',
            {'user_form': user_form, 'occupant_form':occ_form,
            'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('your acct is disabled')
        else:
            print "Invalid credentials: {0}, {1}".format(username, password)
            return HttpResponse("Invalid credentials")
    else:
        return render(request, 'wah_test/login.html', {})

def index(request):
    """
    View for debugging.
    """
    users = Occupant.objects.order_by('user_id')
    context_dict = {'occupants':users, 'boldmessage': "testing some more"}
    return render(request, 'wah_test/index.html',context_dict)
