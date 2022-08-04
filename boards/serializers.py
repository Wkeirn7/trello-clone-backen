from rest_framework import serializers
from .models import Board

class UserBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'board_name', 'description', 'owner']