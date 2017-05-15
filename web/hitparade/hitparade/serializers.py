from rest_framework import serializers
from hitparade.models import Team

class TeamSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
