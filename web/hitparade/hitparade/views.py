from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, status

from hitparade.models import Team, Game
from hitparade.serializers import *


class TeamListView(viewsets.ModelViewSet):
    """
    List games
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializerV1


class GameListView(viewsets.ModelViewSet):
    """
    List games
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializerV1


class PlayerListView(viewsets.ModelViewSet):
    """
    List games
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializerV1
