from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Buses, Passenger, Ticket
from django.db.models import Q
import random
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail #sendEmail
from GetBus.settings import EMAIL_HOST_USER #my email which i save in setting.py variable





# Create your views here.



#--------------ListView ------------------------------------------------------------------------------

# Class ListView to Print all Buses it gives QuerySet
class BusList(ListView):
    model = Buses



#--------------DetailView ------------------------------------------------------------------------------

# Class DetailView to Print only one object of Bus it Give one object 
class BusDetail(DetailView):
    model = Buses
    template_Name = "buses/buses_detail.html"
    context_object_name = 'bus'

  
#----------Bus Type AC/Non Search filter ------------------------------------------------------------------------------

def bus_type_filter(request,BusType):
    
    print(BusType)
    
    if BusType == "AC":
       Bus = Buses.objects.all().filter(Bus_Type = BusType)
    if BusType == "Non-AC":
        Bus = Buses.objects.all().filter(Bus_Type = "Non/AC")
    if BusType == "All":
        print("hello")
        Bus = Buses.objects.all()

    return render(request,"buses/bus_type.html", {"Bus": Bus})






#----------Creating Search filter Function ------------------------------------------------------------------------------

def search(request):
    source = request.GET.get("from")
    destination = request.GET.get("to")
    date = request.GET.get("date")

    Bus = Buses.objects.all().filter(Q(From__icontains= source) & Q(To__icontains= destination) & Q(Date__icontains= date)  )
   
    return render(request, "buses/search.html", {"Bus":Bus})




#--------- Adding Passenger ------------------------------------------------------------------------------

@login_required(login_url="/login") #login required means it required login to access this function and it will redirect #to link if fail
def add_passenger(request, BusId):

    if request.method == "GET":
        return render(request, "buses/buses_detail.html")
                      
    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        print(name)
    

        #fetch busId 
        Bus = Buses.objects.get(id = BusId)
    
        #adding Passenger details to table
        passenger = Passenger.objects.create( P_Name = name, Age =age, Gender = gender, Bus_id = Bus )

        #request.session["#name"] = obj.id session is to save in variable so that we can fetch data anywhere because request is every where and we can fetch it like this  # To fetch data through request session.get("#name")
        request.session["P_id"] = passenger.id

        return HttpResponseRedirect("/bus/payment/"+str(Bus.id))
#----------Adding Passenger ------------------------------------------------------------------------------


#----------Book Function ------------------------------------------------------------------------------


@csrf_exempt
def book(request, Tickets):
  

    passenger = Passenger.objects.get(id = request.session.get("P_id") )
    
    print("ticket start")
    print(passenger)
    #creating Ticket
    ticket = Ticket.objects.create( User= request.user, Bus=passenger.Bus_id, Name = passenger.P_Name, Age= passenger.Age, Gender= passenger.Gender, Ticket_No = int(Tickets) )
    print("ticket end")

    #send_mail( 'Order Placed ')
    send_mail("GetBus Your Ticket Has Been booked", #subject,
             "Thank You for Using GetBus For booking Bus Tickets Online", #message,
             EMAIL_HOST_USER,#sender
             [ "sohailshaik8910@gmail.com" ], #Receiver
             fail_silently=False)
    
    return render(request,"buses/ticket.html", {"ticket":ticket} )
    #return render(request,"buses/ticket.html")




#----------Create Payment function through Razorpay ------------------------------------------------------------------------------

@csrf_exempt
def payment(request,BusId):
    client = razorpay.Client(auth=("rzp_test_tXhb7aXiGBGPzD", "9tr12zxl6DeyAEAQdkHAGShJ"))


    
    #fetching Bus data using BusId in argument url link to get Bus amount
    Bus = Buses.objects.get(id = BusId)
    amount = Bus.Price*100
    print(amount)

    #Generating Random Ticket Number
    TicketNo = str(random.randint(237382, 963732)*BusId )
    

    data = {"amount": amount, "currency": "INR", "receipt": TicketNo}
    payment = client.order.create(data=data)


    return render(request, "buses/payment.html", {"payment":payment, "TicketNo": TicketNo, "BusId": BusId})


#key_id	= rzp_test_tXhb7aXiGBGPzD  --  key_secret = 9tr12zxl6DeyAEAQdkHAGShJ


