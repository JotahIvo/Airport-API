from django.db import models
from airports.models import Airports
from airline.models import Airline


class Flights(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT, related_name='flights')
    aircraft_name       = models.CharField(max_length=100, blank=True, null=True)
    date                = models.CharField(max_length=50, blank=True, null=True)
    origin_airport      = models.ForeignKey(Airports, on_delete=models.PROTECT, related_name='origin_airport')
    destiny_airport     = models.ForeignKey(Airports, on_delete=models.PROTECT, related_name='destiny_airport')
    price               = models.FloatField(default=0.0, blank=True, null=True)

    def __str__(self):
        return f"{self.aircraft_name} - {self.origin_airport} to {self.destiny_airport}"
        