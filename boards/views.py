from rest_framework import viewsets
from .models import Board, List, Card
from .serializers import UserBoardSerializer, ListSerializer, CardSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserBoardsViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = UserBoardSerializer
    permission_classes = IsAuthenticated

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = IsAuthenticated

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = IsAuthenticated
