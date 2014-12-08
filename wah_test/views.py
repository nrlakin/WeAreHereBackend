from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from wah_test.models import CheckIn, Occupant
#from wah_test.serializers import CheckInSerializer, OccupantSerializer
from wah_test.serializers import *
from knn_classifier import *

# Create your views here.
class Location(APIView):
    """
    Get location from beacon ranges.
    """
    def post(self, request, format=None):
        serializer = BeaconSerializer(data = request.DATA, many = True)
        if serializer.is_valid():
            location = KNNClassifier().get_room(serializer.data)
            return Response(status = location)
        return Response(status = status.HTTP_204_NO_CONTENT)

class Occupancy(APIView):
    """
    Add new occupant or get list of current occupants.
    """
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
