from django.shortcuts import render

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
