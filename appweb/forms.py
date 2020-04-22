"""
Fichier de formulaire Html
"""

from django import forms
from appweb.models import *


# Formulaire
class FormModulaTournoi(forms.Form):
    nombre_joueur = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'min': "2", 'max': "10", 'value': "2"}))
    temps_blinds = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'step': '300', 'value': '00:05'}))
    cave = forms.IntegerField(min_value=1)
    temps_recave = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800', 'value': '00:30'}))


class FormulaireTest(forms.Form):
    nombre_joueur = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'min': "2", 'max': "10", 'value': "2"}))
    temps_blinds = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'step': '300', 'value': '00:05'}))
    cave = forms.IntegerField(min_value=1)
    temps_recave = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800', 'value': '00:30'}))
    print(temps_blinds)
