from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, status

from hitparade.models import Team, Game
from hitparade.serializers import *


class TeamListView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializerV1


class GameListView(viewsets.ModelViewSet):
    serializer_class = GameSerializerV1


    def get_queryset(self):


        filter_kwargs = {
            'status': Game.STATUS_UPCOMING
        }

        if 'status' in self.request.query_params and self.request.query_params['status'] in Game.STATUSES:
            filter_kwargs['status'] = self.request.query_params['status']

        return Game.objects.filter(**filter_kwargs).order_by('started_at')


class PlayerListView(viewsets.ModelViewSet):
    """
    List games
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializerV1
