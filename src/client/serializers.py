from rest_framework import serializers
from .models import User, Game

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'game')

class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name')