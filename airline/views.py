from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from airline.models import Airline
from airline.serializers import AirlineSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AirlineCreateListView(generics.ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AirlineRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = [permissions.IsAuthenticated]
