from rest_framework import viewsets
from .models import Board, List, Card, Person
from .serializers import UserBoardSerializer, ListSerializer, CardSerializer, PersonSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserBoardsViewSet(viewsets.ModelViewSet):
    serializer_class = UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = IsAuthenticated

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = IsAuthenticated

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = IsAuthenticated
