from django.urls import path
from . import views


urlpatterns = [
    path('airline/', views.AirlineCreateListView.as_view(), name='airport-list-view'),
    path('airline/<int:pk>/', views.AirlineRetrieveUpdateDestroyView.as_view(), name='airport-detail')
]
