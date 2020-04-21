from django.shortcuts import render
from appweb.forms import *
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
        'forms': FormulaireTest,
        'forms1': FormulaireTestMeta,
    }
    return render(request, 'appweb.testviewweb.html',content )
