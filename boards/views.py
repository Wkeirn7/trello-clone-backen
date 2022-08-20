from rest_framework import viewsets
from .models import Board, List, Card, Person
from .serializers import UserBoardSerializer, ListSerializer, CardSerializer, PersonSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import json

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

    def get_queryset(self):
        return Board.objects.filter(id=self.kwargs['pk'])

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
        return List.objects.filter(board=self.kwargs['boards_list_pk'], id=self.kwargs['pk'])

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, boards_list_pk=None, lists_pk=None):
        queryset = Card.objects.filter(associated_list=lists_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, boards_list_pk=None, pk=None, lists_pk=None):
        queryset = Card.objects.filter(associated_list=lists_pk)
        card = get_object_or_404(queryset, pk=pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def perform_create(self, serializer):
        associated_list = List.objects.get(id=self.kwargs['lists_pk'])
        return serializer.save(associated_list=associated_list)

    def get_queryset(self):
        return Card.objects.filter(associated_list=self.kwargs['lists_pk'], id=self.kwargs['pk'])

class BoardPersonViewSet(viewsets.ViewSet):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def list(self, *args, **kwargs):
        board = Board.objects.get(id=kwargs['boards_list_pk'])
        queryset = board.participants.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
        
        board = Board.objects.get(id=kwargs['boards_list_pk'])

        request_uni = self.request.body.decode('utf-8')
        body = json.loads(request_uni)
        print(body)
        first_name = body['first_name']
        last_name = body['last_name']
        person = Person(first_name=first_name, last_name=last_name)
        person.save()

        board.participants.add(person)

        serializer = PersonSerializer(board.participants.all(), many=True)
        return Response(serializer.data)

    def destroy(self, *args, **kwargs):
        board = Board.objects.get(id=kwargs['boards_list_pk'])
        person = Person.objects.get(id=kwargs['pk'])
        person.delete()
        serializer = PersonSerializer(board.participants.all(), many=True)
        return Response(serializer.data)

class CardPersonViewSet(viewsets.ViewSet):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def list(self, *args, **kwargs):
        card = Card.objects.get(id=kwargs['cards_pk'])
        queryset = card.assigned_to.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, *args, **kwargs):
            queryset = Person.objects.filter(associated_list=lists_pk)
            card = get_object_or_404(queryset, pk=pk)
            serializer = CardSerializer(card)
            return Response(serializer.data)

    def create(self, *args, **kwargs):

        board = Board.objects.get(id=kwargs['boards_list_pk'])
        card = Card.objects.get(id=kwargs['cards_pk'])
        
        request_uni = self.request.body.decode('utf-8')
        body = json.loads(request_uni)
        person_id = body['id']
        person = board.participants.get(id=person_id)

        card.assigned_to.add(person)

        serializer = PersonSerializer(card.assigned_to.all(), many=True)
        return Response(serializer.data)

    def destroy(self, *args, **kwargs):
        card = Card.objects.get(id=kwargs['cards_pk'])
        person = Person.objects.get(id=kwargs['pk'])
        person.delete()
        serializer = PersonSerializer(board.participants.all(), many=True)
        return Response(serializer.data)


        
