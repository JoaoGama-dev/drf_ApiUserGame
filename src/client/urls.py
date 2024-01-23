from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserViewSet, 'user')
router.register('game', views.UserViewSet, 'game')

urlpatterns = [
    *router.urls
]

