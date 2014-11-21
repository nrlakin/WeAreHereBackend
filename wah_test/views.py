from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from wah_test.models import CheckIn, Occupant
from wah_test.serializers import CheckInSerializer, OccupantSerializer

# Create your views here.

@api_view(['GET','POST'])
def occupancy(request):
    """
    Add new occupant or get list of current occupants.
    """
    if request.method == 'GET':
        occupants = Occupant.objects.all()
        serializer = OccupantSerializer(occupants, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OccupantSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def update(request, id):
    """
    Update, retrieve, or delete a single user.
    """
    try:
        occupant = Occupant.objects.get(pk = id)
    except Occupant.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OccupantSerializer(occupant, data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = OccupantSerializer(occupant)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        occupant.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
