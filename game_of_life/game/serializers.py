from rest_framework import serializers

from .models import GameSavings


class GameSavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSavings
        fields = ('grid_state',)
