from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from . models import HotelPost
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})

#def places(request):
#	return render(request, 'places.html', {})

#def hotel(request):
#	return render(request, 'hotel.html', {})


class PlacesView(ListView):
	"""docstring for PlacesView"""
	model = Post
	template_name = 'places.html'
	ordering = ['-id']
	paginate_by = 6


class TourDetailsView(DetailView):
	model = Post
	template_name = 'tour_details.html'


# sending email
def contact(request):

	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']

		# send email
		send_mail(
			message_subject, #subject
			message, # message text
			message_email, # from message
			['uzsayyortravel@gmail.com'], # to message
			fail_silently=False,

			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})
		

class HotelsView(ListView):
	"""docstring for PlacesView"""
	model = HotelPost
	template_name = 'hotel.html'
	ordering = ['-id']
	paginate_by = 6

class HotelDetailsView(DetailView):
	model = HotelPost
	template_name = 'hotel_details.html'