from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, status

from hitparade.models import Team, Game
from hitparade.serializers import TeamSerializerV1, GameSerializerV1


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
