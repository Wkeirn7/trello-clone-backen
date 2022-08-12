from rest_framework import serializers
from .models import Board, List, Card, Person

class UserBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'board_name', 'description', 'participants', 'owner']
        read_only_fields = ['owner']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'list_name', 'board']
        read_only_fields = ['board']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'intro', 'description', 'created_on']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name']