from rest_framework import serializers
from hitparade.models import Team, Game, Player, GameStat

class TeamSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class GameSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class PlayerSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class GameStatSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = GameStat
        fields = '__all__'
