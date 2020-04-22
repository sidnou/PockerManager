from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
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
        'forms': "",

    }
    # Verification de method P
    if request.method == 'POST':
        form0 = FormModulaTournoi(request.POST)
        print(form0)
        content['forms'] = form0

        if form0.is_valid():
            n_gamer = form0.cleaned_data['nombre_joueur']
            print(n_gamer)
            t_blinds = form0.cleaned_data['temps_blinds']
            print(type(form0.cleaned_data['temps_blinds']))
            content['valeurTemp'] = t_blinds
            # return render(request,'appweb/index.html', content)
            # return HttpResponseRedirect(reverse('home'))
    else:
        form0 = FormModulaTournoi()
        content['forms'] = form0

    return render(request, 'appweb/index.html', content)


def createTournois(request):
    content = {
        'title': "Poker Manager",
        'version': VERSION,
        'author': AUTHOR,
        'forms': "",
    }

    # Verification de method POST
    if request.method == 'POST':
        form = FormModulaTournoi(request.POST)
        print(form)
        content['forms'] = form

        if form.is_valid():
            return HttpResponseRedirect(reverse('home'))
    else:
        form = FormModulaTournoi()
        content['forms'] = form

    return render(request, 'appweb/create-tournoi.html', content)


##################################################################################################################
##################################################################################################################
#                           PARTIT TESTE
##################################################################################################################
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
