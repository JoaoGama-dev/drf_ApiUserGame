from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Games
from .serializers import UserSerializer, GamerSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GamerView(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamerSerializer