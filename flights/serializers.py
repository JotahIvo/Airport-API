from rest_framework import serializers
from flights.models import Flights


class FlightsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flights
        fields = '__all__'
