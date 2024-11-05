from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from airports.models import Airports
from airline.models import Airline
from flights.models import Flights
from airports.serializers import AirportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@method_decorator(csrf_exempt, name='dispatch')
class AirportCreateListView(generics.ListCreateAPIView):
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AirportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [permissions.IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')
class AirlineAirportsView(APIView):
    def get(self, request, *args, **kwargs):
        airlines_data = []

        # Para cada companhia aérea, coletar os aeroportos associados
        for airline in Airline.objects.all():
            # Obter os aeroportos de origem e destino de todos os voos da companhia aérea
            origin_airports = Flights.objects.filter(airline=airline).values_list('origin_airport', flat=True).distinct()
            destiny_airports = Flights.objects.filter(airline=airline).values_list('destiny_airport', flat=True).distinct()

            # Combinar aeroportos de origem e destino em um único conjunto para evitar duplicação
            all_airports = Airports.objects.filter(id__in=set(list(origin_airports) + list(destiny_airports)))

            # Serializar os dados
            airline_data = {
                'airline': airline.name,
                'airports': [{'name': airport.name, 'city': airport.city, 'country': airport.country} for airport in all_airports]
            }
            airlines_data.append(airline_data)

        return Response(airlines_data)


@method_decorator(csrf_exempt, name='dispatch')
class AvailableDestinationsView(APIView):
    def get(self, request, origin_airport_id, *args, **kwargs):
        try:
            # Verifica se o aeroporto de origem existe
            origin_airport = Airports.objects.get(id=origin_airport_id)

            # Filtra os voos com base no aeroporto de origem e obtém os aeroportos de destino distintos
            destination_airports = Airports.objects.filter(
                id__in=Flights.objects.filter(origin_airport=origin_airport).values_list('destiny_airport', flat=True).distinct()
            )

            # Serializa os dados dos aeroportos de destino
            destinations = [{'name': airport.name, 'city': airport.city, 'country': airport.country} for airport in destination_airports]

            return Response({
                'origin_airport': origin_airport.name,
                'destinations': destinations
            }, status=status.HTTP_200_OK)

        except Airports.DoesNotExist:
            return Response({
                "error": "Origin airport not found."
            }, status=status.HTTP_404_NOT_FOUND)
