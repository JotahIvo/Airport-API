from django.urls import path
from .views import TicketPurchaseView


urlpatterns = [
    path('purchase-ticket/', TicketPurchaseView.as_view(), name='purchase-ticket')
]
