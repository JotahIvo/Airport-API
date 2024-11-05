from rest_framework import serializers
from airports.models import Airports


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airports
        fields = '__all__'
