from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from flights.models import Flights
from flights.serializers import FlightsSerializer


@method_decorator(csrf_exempt, name='dispatch')
class FlightsCreateListView(generics.ListCreateAPIView):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer


@method_decorator(csrf_exempt, name='dispatch')
class FlightsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer
    permission_classes = [permissions.IsAuthenticated]
