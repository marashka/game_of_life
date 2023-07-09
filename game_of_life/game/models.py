from django.db import models


class GameSavings(models.Model):
    grid_state = models.JSONField(
        verbose_name='Состояние сетки',
    )
