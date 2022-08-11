from rest_framework import serializers
from .models import Board, List, Card

class UserBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'board_name', 'description', 'owner']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'list_name']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'intro', 'description', 'created_on']