from rest_framework import serializers
from hitparade.models import Team, Game

class TeamSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class GameSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
