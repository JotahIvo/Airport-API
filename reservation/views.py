import random, string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Flights, Reservation
from .serializers import ReservationSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TicketPurchaseView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        user = request.user
        flight_id = request.data.get('flight_id')
        num_passengers = request.data.get('num_passengers')

        # Valida o número de passageiros
        if not num_passengers or int(num_passengers) <= 0:
            return Response({"error": "Invalid number of passengers."}, status=status.HTTP_400_BAD_REQUEST)

        # Tenta buscar o voo especificado
        try:
            flight = Flights.objects.get(id=flight_id)
        except Flights.DoesNotExist:
            return Response({"error": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)

        # Calcula o preço total
        total_price = flight.price * int(num_passengers)

        # Gera o localizador da reserva e o número do e-ticket
        locator = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        e_ticket_number = ''.join(random.choices(string.digits, k=12))

        # Cria a reserva
        reservation = Reservation.objects.create(
            user=user,
            flight=flight,
            locator=locator,
            e_ticket_number=e_ticket_number,
            num_passengers=num_passengers,
            total_price=total_price
        )

        # Serializa a reserva e retorna a resposta
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
