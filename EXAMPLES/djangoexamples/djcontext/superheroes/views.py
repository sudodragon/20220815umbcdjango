from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render


def home(request):
    """
    Main page of site

    :param request: HTTP request
    :return: HTTP Response with a message
    """
    return HttpResponse("Welcome to the superhero app")

def secret_word(request):
    data = {'message': "Getting a secret word from settings.py via a context processor"}
    return render(request, 'superheroes/secret_word.html', data)

def random_word(request):
    data = {'message': "Getting a random word via a context processor"}
    return render(request, 'superheroes/random_word.html', data)


def request_dump(request):
    data = {'message': "Dumping the request object via a context processor"}
    return render(request, 'superheroes/request_dump.html', data)

