from django.conf import settings

from game_logic.game_logic import GameOfLife, Grid
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GameSavings
from .serializers import GameSavingsSerializer

GAME_GRID_HEIGHT: int = settings.GAME_GRID_HEIGHT
GAME_GRID_WIDTH: int = settings.GAME_GRID_WIDTH


@api_view(['GET'])
def game_of_life_view(request):
    game = GameOfLife(GAME_GRID_WIDTH, GAME_GRID_HEIGHT)
    if GameSavings.objects.exists():
        game_savings = GameSavings.objects.first()
        unloaded_grid_state: Grid = game_savings.grid_state
        game.load_grid_state(unloaded_grid_state)
        game.make_step()
        new_grid_state: Grid = game.get_grid_state()
        game_savings.grid_state = new_grid_state
        game_savings.save()
        if unloaded_grid_state == new_grid_state:
            game_savings.delete()
            return Response('Конец игры, клетки не поменяли своего положения', status=status.HTTP_200_OK)
        if game.is_all_dead:
            game_savings.delete()
            return Response('Конец игры, все мертвы', status=status.HTTP_200_OK)
        serializer = GameSavingsSerializer(game_savings)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    initial_grid_state: Grid = game.get_grid_state()
    game.savings = GameSavings.objects.create(grid_state=initial_grid_state)
    serializer = GameSavingsSerializer(game.savings)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
