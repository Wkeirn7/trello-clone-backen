from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Board(models.Model):
    board_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    participants = models.ManyToManyField(Person, related_name='board_participants', blank=True)

class List(models.Model):
    list_name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')

class Card(models.Model):
    intro = models.TextField()
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards', blank=True)
    associated_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
