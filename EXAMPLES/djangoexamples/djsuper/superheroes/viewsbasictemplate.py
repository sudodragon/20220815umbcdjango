from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Superhero
from pdb import set_trace
def hero_basic_template(request, hero_name):
    # set_trace()
    hero =  get_object_or_404(Superhero, name=hero_name)
    # raise Http404("You are poking around in the wrong place, buckaroo")
    context = {
        'hero_name': hero.name,
        'real_name': hero.real_name,
        'secret_identity': hero.secret_identity,
    }
    return render(request, 'superheroes/hero_basic.html', context)
