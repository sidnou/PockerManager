from django.shortcuts import render
from appweb.forms import *
from appweb.models import *
import datetime

# Variables CONSTANTS
VERSION = '0.0.1'
AUTHOR = "Jacques-andré S"


# Create your views here.
def index(request):
    content = {
        'title': "Poker Manager",
        'version': VERSION,
        'author': AUTHOR,
        'valeurTemp': "00h15",
        'valeurSmBlind': "5",
        'valeurBigBlind': "10",

    }

    return render(request, 'appweb/index.html', content)


# Page teste de vue web
def testviewweb(request):
    content = {
        'title': "Poker Manager",
        'version': VERSION,
        'author': AUTHOR,
        'valeurTemp': "00h15",
        'valeurSmBlind': "5",
        'valeurBigBlind': "10",
        'forms': '',
    }
    if request.method == 'POST':
        forms_test = FormulaireTest(request.POST)
        print(forms)
        content['forms'] = forms_test
        if forms_test.is_valid():
            print('nombre de joueurs:', forms_test.cleaned_data['nombre_joueur'])
            print('temps des blinds:', forms_test.cleaned_data['temps_blinds'])
            nombre_joueurs = Joueurs(nombre_joueur=forms_test.cleaned_data['nombre_joueur'])
            nombre_joueurs.save()
            temps_blinds = forms_test.cleaned_data['temps_blinds'].minute * 2
            print(temps_blinds)




    else:
        forms_test = FormulaireTest()
        content['forms'] = forms_test

    return render(request, 'appweb/testviewweb.html', content)
