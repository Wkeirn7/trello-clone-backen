from rest_framework import viewsets
from .models import Board, List, Card
from .serializers import UserBoardSerializer, ListSerializer, CardSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserBoardsViewSet(viewsets.ModelViewSet):
    serializer_class = UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def create(self):
        pass

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = IsAuthenticated

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = IsAuthenticated
