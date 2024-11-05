from django.db import models
#from flights.models import Flights

class Airline(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    #flights = models.ForeignKey(Flights, on_delete=models.PROTECT, related_name='airline')

    def __str__(self):
        return self.name

    """ def get_destinations_from_origin(self, origin_airport):
        return Flights.objects.filter(origin_airport=origin_airport).values('destiny_airport').distinct() """
 