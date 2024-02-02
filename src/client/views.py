from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Game
from .serializers import UserSerializer, GamerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GamerViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GamerSerializer