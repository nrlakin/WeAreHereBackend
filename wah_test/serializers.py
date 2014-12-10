from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from wah_test.models import CheckIn, Occupant

class Beacon(object):

    def __init__(self, beacon_id, rssi):
        self.beacon_id = beacon_id
        self.rssi = rssi

    def to_dict(self):
        return {'beacon_id':beacon_id, 'rssi':self.rssi}

class CheckInSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CheckIn
        fields = ('user','room_id','when')

class UserSerializer(serializers.ModelSerializer):
    checkins = serializers.PrimaryKeyRelatedField(many = True,
                                        queryset = CheckIn.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'checkins')

class OccupantSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='user.username')
    class Meta:
        model = Occupant
        fields = ('id', 'name', 'room_id')
        depth = 1

class BeaconSerializer(serializers.Serializer):
    beacon_id = serializers.CharField(required=True, max_length = 40)
    rssi = serializers.IntegerField()

    def create(self, validated_data):
        return Beacon(**validated_data)
