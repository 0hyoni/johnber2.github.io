from django.contrib import admin
from .models import Blog
from .models import Movie
from .models import Music
# Register your models here.
admin.site.register(Blog)
admin.site.register(Movie)
admin.site.register(Music)