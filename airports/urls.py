from django.urls import path
from . import views


urlpatterns = [
    path('airports/', views.AirportCreateListView.as_view(), name='airport-list-view'),
    path('airports/<int:pk>/', views.AirportRetrieveUpdateDestroyView.as_view(), name='airport-detail'),
    path('airlines/airports/', views.AirlineAirportsView.as_view(), name='airline-airports'),
    path('airports/<int:origin_airport_id>/destinations/', views.AvailableDestinationsView.as_view(), name='available-destinations'),
]
