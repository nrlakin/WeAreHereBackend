from django.forms import widgets
from rest_framework import serializers
from wah_test.models import CheckIn, Occupant

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('id', 'name', 'room','when')

class OccupantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupant
        fields = ('id', 'name', 'room')
        read_only_fields = ('name', 'id',)
