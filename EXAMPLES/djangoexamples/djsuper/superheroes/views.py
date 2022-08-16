from django.http import HttpResponse
from .models import Superhero

def home(request):
    """
    Home page of the Superheroes app

    :param request: HTTP request
    :return: HTTP Response with displayable text
    """
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    # etc etc
    return HttpResponse("Welcome to the superhero app "  + request.method  )

def hero(request, hero_name):
    """
    Display name and secret identity

    :param request: HTTP request
    :param hero_name: name of hero (str)
    :return: HTTP Response with displayable text
    """
    s = Superhero.objects.get(name=hero_name)
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name)
    )

def hero_int(request, hero_num):
    return HttpResponse("hero_int view " + str(hero_num * 2))
def hero_str(request, hero_text):
    return HttpResponse("hero_str view: " + hero_text)
