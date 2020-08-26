from django.contrib import admin
from .models import Post
from . models import HotelPost

# Register your models here.
admin.site.register(Post)
admin.site.register(HotelPost)