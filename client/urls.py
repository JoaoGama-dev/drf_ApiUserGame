from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Users', views.UserView)
router.register('Games', views.GamerView)

urlpatterns = [
    path('', include(router.urls))
]

