from django.shortcuts import render
from rest_framework import viewsets
from .models import Board
from .serializers import UserBoardSerializer

# Create your views here.
class UserBoardsViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = UserBoardSerializer