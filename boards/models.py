from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    board_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')

class List(models.Model):
    list_name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')

class Card(models.Model):
    content = models.TextField()
    associated_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
