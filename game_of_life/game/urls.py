from django.urls import path

from .views import game_of_life_view

app_name = 'game_of_life'

urlpatterns = [
    path('game_of_life/', game_of_life_view, name='start')
]
