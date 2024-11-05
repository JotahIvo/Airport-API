from django.urls import path
from . import views


urlpatterns = [
    path('flights/', views.FlightsCreateListView.as_view(), name='flights-list-view'),
    path('flights/<int:pk>/', views.FlightsRetrieveUpdateDestroyView.as_view(), name='flights-detail')
]
