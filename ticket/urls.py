from django.urls import path
from .views import TicketList, TicketDetail
from . import views

urlpatterns = [
    
    path('tickets/',TicketList.as_view(), name="tickets" ),
    path('cancel-ticket/<int:ticketId>', views.Cancel_Ticket, name="cancel-ticket" ),
    path('view-ticket/<int:pk>', TicketDetail.as_view(), name="ticket-detail" ),
]
