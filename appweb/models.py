from django.db import models

# Variable
COLOR_JETONS = [('RED', 'Rouge'), ('BLUE', 'Bleu'), ('GREEN', 'Vert'), ('BLACK', 'Noir'), ('BROWN', 'Marron'),
                ('ORANGE', 'Orange')]


# Create your models here.
# Tableua de
class Joueurs(models.Model):
    nombre_joueur = models.IntegerField()


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


# Tableau tournois     <<< mettre à jour le table Tournois
class Tournois(models.Model):
    name_tournoi = models.CharField(max_length=25,null=False)
    n_game = models.ForeignKey(Joueurs, on_delete=models.CASCADE)
    t_game = models.ForeignKey(Blinds, on_delete=models.CASCADE)
