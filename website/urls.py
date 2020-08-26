from django.urls import path
from . import views
from . views import PlacesView, TourDetailsView, HotelsView, HotelDetailsView

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    #path('places.html', views.places, name="places"),
    #path('hotel.html', views.hotel, name="hotel"),
    path('places.html', PlacesView.as_view(), name="places"),
    path('tour_details/<int:pk>', TourDetailsView.as_view(), name="tour_details"),

    path('hotel.html', HotelsView.as_view(), name="hotel"),
    path('hotel_details/<int:pk>', HotelDetailsView.as_view(), name="hotel_details"),
]
