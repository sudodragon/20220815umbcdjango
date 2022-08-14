from django.http import HttpResponse
from .models import Superhero

#TODO: actually use sessions

def home(request):
    return HttpResponse("Welcome to the superhero app")

def hero(request, hero_name):
    s = Superhero.objects.get(name=hero_name)
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name)
    )

