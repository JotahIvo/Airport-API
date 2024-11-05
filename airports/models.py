from django.db import models


class Airports(models.Model):
    name        = models.CharField(max_length=100, blank=True, null=True)
    country     = models.CharField(max_length=200, blank=True, null=True)
    city        = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    