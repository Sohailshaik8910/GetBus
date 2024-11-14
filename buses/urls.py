from django.urls import path
from .views import BusList, BusDetail, search, book, bus_type_filter, payment
from .views import add_passenger



urlpatterns = [

    path('list/', BusList.as_view(), name ="list"),
    path('detail/<int:pk>', BusDetail.as_view(), name="detail" ),
    path('search/', search, name='search'),
    path('book/<slug:Tickets>', book, name="book"),
    path('bus-type/<str:BusType>', bus_type_filter, name="bus-type" ),
    path('payment/<int:BusId>', payment, name="payment"),
    path('passenger-detail/<int:BusId>', add_passenger, name="add-passenger")
     
]

