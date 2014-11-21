from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wah_test.models import CheckIn, Occupant
from wah_test.serializers import CheckInSerializer, OccupantSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def occupancy(request):
    """
    Add new occupant or get list of current occupants.
    """
    if request.method == 'GET':
        occupantss = Occupant.objects.all()
        serializer = OccupantSerializer(occupants, many = True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OccupantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201)
        return JSONResponse(serializer.errors, status = 400)

@csrf_exempt
def update(request, id):
    """
    Update, retrieve, or delete a single user.
    """
    try:
        occupant = Occupant.objects.get(pk = id)
    except Occupant.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OccupantSerializer(occupant, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201)
        return JSONResponse(serialzer.errors, status = 400)

    elif request.method == 'GET':
        serializer = OccupantSerializer(occupant)
        return JSONResponse(serializer.data)

    elif request.method == 'DELETE':
        occupant.delete()
        return JSONResponse(status = 204)
