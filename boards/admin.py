from django.contrib import admin
from .models import List, Board, Card

# Register your models here.
admin.site.register([List, Board, Card])