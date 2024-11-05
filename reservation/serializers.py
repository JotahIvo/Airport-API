from rest_framework import serializers
from .models import Reservation, Flights


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['locator', 'e_ticket_number', 'num_passengers', 'total_price', 'purchase_date']
