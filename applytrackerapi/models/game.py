from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=155)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_creator') #creator of game
    game_type = models.ForeignKey("GameType", null=True, blank=True, on_delete=models.CASCADE, related_name='game_type')
    description = models.CharField(max_length=155)
    maker = models.CharField(max_length=155, null=True)
    skill_level = models.CharField(max_length=155)
    number_of_players = models.IntegerField()