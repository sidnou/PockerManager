"""
Fichier de formulaire Html
"""

from django import forms
from django.forms import ModelForm
from appweb.models import *


# Formulaire
class FormulaireTest(forms.Form):
    nombre_joueur = forms.IntegerField(max_value=10, min_value=2)
    temps_blinds = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'step': '300', 'value': '00:00'}))
    print(temps_blinds)


class FormulaireTestMeta(ModelForm):
    class Meta:
        model = Joueurs
        fields = '__all__'
        # widgets = {'nombre_joueur':IntegerField(attrs={max_value=10, min_value=2})  }
