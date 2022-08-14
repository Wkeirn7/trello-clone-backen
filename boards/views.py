from rest_framework import viewsets
from .models import Board, List, Card, Person
from .serializers import UserBoardSerializer, ListSerializer, CardSerializer, PersonSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.
class UserBoardsViewSet(viewsets.ModelViewSet):
    serializer_class = UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request,):
        queryset = Board.objects.filter(owner=request.user)
        serializer = UserBoardSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Board.objects.filter(owner=request.user)
        board = get_object_or_404(queryset, pk=pk)
        serializer = UserBoardSerializer(board)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, boards_list_pk=None):
        queryset = List.objects.filter(board=boards_list_pk)
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, boards_list_pk=None):
        queryset = List.objects.filter(pk=pk, board=boards_list_pk)
        list_obj = get_object_or_404(queryset, pk=pk)
        serializer = ListSerializer(list_obj)
        return Response(serializer.data)

    def perform_create(self, serializer):
        print(self.kwargs['boards_list_pk'])
        board = Board.objects.get(id=self.kwargs['boards_list_pk'])
        return serializer.save(board=board)

    def get_queryset(self):
        print(self.kwargs)
        return List.objects.filter(board=self.kwargs['boards_list_pk'], id=self.kwargs['pk'])

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
