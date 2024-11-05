from django.db import models
from django.conf import settings
from flights.models import Flights


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE, related_name='reservations')
    locator = models.CharField(max_length=10, unique=True)
    e_ticket_number = models.CharField(max_length=12, unique=True)
    num_passengers = models.PositiveIntegerField()
    total_price = models.FloatField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation {self.locator} for {self.user}"
