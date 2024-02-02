from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=250)

    # TODO: Isso aqui deveria estar dentro de games, não aqui fora(ok)
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=250)
    games = models.ManyToManyField(Game) #TODO: Mudar esse campo para ManyToManyFields (ver Notas)(ok)

    # TODO: Isso aqui deveria estar dentro de users, não aqui fora(ok)
    def __str__(self):
        return self.name


