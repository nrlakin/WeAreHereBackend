from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from wah_test.models import CheckIn, Occupant
from wah_test.serializers import CheckInSerializer, OccupantSerializer

# Create your views here.

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

    def put(self, request, pk, format=None):
        occupant = self.get_occupant(pk)
        serializer = OccupantSerializer(occupant, data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        occupant = self.get_occupant(pk)
        serializer = OccupantSerializer(occupant)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        occupant = self.get_occupant(pk)
        occupant.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
