from django.shortcuts import render


def index(request):
    return render(request, 'gametemplates/index.html')


def game(request):
    return render(request, 'gametemplates/game.html')
