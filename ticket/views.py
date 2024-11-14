from django.shortcuts import render, HttpResponseRedirect
from buses.models import Ticket
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView




# Create your views here.


#--------------Ticket List------------------------------------------------------------------------------

class TicketList(ListView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "ticket/ticket_list.html"


#--------------Ticket Detail------------------------------------------------------------------------------

class TicketDetail(DetailView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "ticket/ticket_detail.html"

#-------------- Cancel Ticket ------------------------------------------------------------------------------


def Cancel_Ticket(request,ticketId):
   
    print('ticket',ticketId)

    tickets = Ticket.objects.get(id = ticketId)
    print(tickets.Ticket_No)
    tickets.delete()

    return HttpResponseRedirect("/ticket/tickets")