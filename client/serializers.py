from rest_framework import serializers
from .models import User, Games

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'name', 'game')

class GamerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        fields = ('id', 'url', 'name')