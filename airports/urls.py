from django.urls import path
from . import views


urlpatterns = [
    path('airports/', views.AirportCreateListView.as_view(), name='airport-list-view'),
    path('airports/<int:pk>/', views.AirportRetrieveUpdateDestroyView.as_view(), name='airport-detail')
]
