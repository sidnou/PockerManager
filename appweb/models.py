from django.db import models

# Variable
COLOR_JETONS = [('RED', 'Rouge'), ('BLUE', 'Bleu'), ('GREEN', 'Vert'), ('BLACK', 'Noir'), ('BROWN', 'Marron'),
                ('ORANGE', 'Orange')]


# Create your models here.
# Tableua de
class Joueurs(models.Model):
    nombreJoueur = models.IntegerField(max_length=2,)

# Tableau Jetons
class Jetons(models.Model):
    color = models.CharField(choices=COLOR_JETONS, max_length=25)
    value = models.IntegerField()
    nombre_jeton = models.IntegerField()


# Tebleau Blinds
class Blinds(models.Model):
    times = models.TimeField()
    smallBlind = models.IntegerField()
    bigBlind = models.IntegerField()
