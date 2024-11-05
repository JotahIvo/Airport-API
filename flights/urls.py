from django.urls import path
from . import views


urlpatterns = [
    path('flights/', views.FlightsCreateListView.as_view(), name='flights-list-view'),
    path('flights/<int:pk>/', views.FlightsRetrieveUpdateDestroyView.as_view(), name='flights-detail'),
    path('flights/<str:flight_date>/', views.AvailableFlightsView.as_view(), name='available-flights'),
    path('flights/cheapest/<int:num_passengers>/', views.CheapestFlightsView.as_view(), name='cheapest-flights'),
]
