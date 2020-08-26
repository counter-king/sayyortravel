from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.

class Post(models.Model):
	news_image = models.ImageField(null=True, blank=True, upload_to="images/")
	place_name = models.CharField(max_length=255)
	price = models.CharField(max_length=255)
	duration = models.CharField(max_length=255)
	news_image2 = models.ImageField(null=True, blank=True, upload_to="images/")
	news_image3 = models.ImageField(null=True, blank=True, upload_to="images/")
	news_image4 = models.ImageField(null=True, blank=True, upload_to="images/")
	news_image5 = models.ImageField(null=True, blank=True, upload_to="images/")


	def __str__(self):
		return self.place_name

class HotelPost(models.Model):
	hotel_image = models.ImageField(null=True, blank=True, upload_to="images/")
	hotel_image2 = models.ImageField(null=True, blank=True, upload_to="images/")
	hotel_image3 = models.ImageField(null=True, blank=True, upload_to="images/")
	hotel_image4 = models.ImageField(null=True, blank=True, upload_to="images/")
	hotel_name = models.CharField(max_length=255)
	hotel_price = models.CharField(max_length=255)
	hotel_address = models.CharField(max_length=255)
	hotel_description = models.TextField()
	hotel_to_center = models.CharField(max_length=255)
	hotel_to_airport = models.CharField(max_length=255)
	hotel_near_sightseeings = models.CharField(max_length=255)

	def __str__(self):
		return self.hotel_name

		