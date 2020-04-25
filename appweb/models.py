from django.db import models

# Variable
COLOR_JETONS = [('RED', 'Rouge'), ('BLUE', 'Bleu'), ('GREEN', 'Vert'), ('BLACK', 'Noir'), ('BROWN', 'Marron'),
                ('ORANGE', 'Orange')]


# Create your models here.
# Tableua de
class Joueurs(models.Model):
    nom_joueur = models.CharField(max_length=25)



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
    nombre_joueur = models.IntegerField()
    temps_blinds = models.DateTimeField(null=True)
    cave = models.IntegerField(null=True)
    temps_recave = models.DateTimeField(null=True)


# # Tableau journal Poker Manager
# class PokerManagerLog(models.Model):
#     message = models.TextField()
#     type_journal = models.CharField(max_length=50)
#     date_journal = models.DateField(auto_now=True)
