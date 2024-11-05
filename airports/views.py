from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from airports.models import Airports
from airports.serializers import AirportSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AirportCreateListView(generics.ListCreateAPIView):
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AirportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [permissions.IsAuthenticated]
