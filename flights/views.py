from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from flights.models import Flights
from flights.serializers import FlightsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@method_decorator(csrf_exempt, name='dispatch')
class FlightsCreateListView(generics.ListCreateAPIView):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer


@method_decorator(csrf_exempt, name='dispatch')
class FlightsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer
    permission_classes = [permissions.IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')
class AvailableFlightsView(APIView):
    def get(self, request, flight_date, *args, **kwargs):
        # Filtra os voos com base na data especificada
        flights = Flights.objects.filter(date=flight_date)
        
        # Verifica se há voos para a data especificada
        if not flights.exists():
            return Response({
                "message": "No flights available for the specified date."
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Serializa os dados dos voos encontrados
        serializer = FlightsSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@method_decorator(csrf_exempt, name='dispatch')
class CheapestFlightsView(APIView):
    def get(self, request, num_passengers, *args, **kwargs):
        try:
            # Converte o número de passageiros para inteiro
            num_passengers = int(num_passengers)

            # Filtra os voos disponíveis e ordena pelo preço
            flights = Flights.objects.all().order_by('price')

            # Verifica se há voos disponíveis
            if not flights.exists():
                return Response({
                    "message": "No flights available."
                }, status=status.HTTP_404_NOT_FOUND)

            # Serializa os dados dos voos mais baratos
            cheapest_flights = []
            for flight in flights:
                # Calcula o custo total para o número de passageiros
                total_price = flight.price * num_passengers
                flight_data = {
                    "aircraft_name": flight.aircraft_name,
                    "origin_airport": flight.origin_airport.name,
                    "destiny_airport": flight.destiny_airport.name,
                    "price_per_passenger": flight.price,
                    "total_price": total_price
                }
                cheapest_flights.append(flight_data)

            return Response(cheapest_flights, status=status.HTTP_200_OK)

        except ValueError:
            return Response({
                "error": "Invalid number of passengers."
            }, status=status.HTTP_400_BAD_REQUEST)
        