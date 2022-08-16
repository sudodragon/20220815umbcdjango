#!/usr/bin/env python
#
from django.shortcuts import get_object_or_404, render
from .models import Superhero
from django.http import HttpResponse, Http404
from django.template.loader import get_template

def hero_hard_way(request, hero_name):
    try:
        hero = Superhero.objects.get(name=hero_name)
    except Exception as err:
        raise Http404(err)

    data = {
        'hero_name': hero.name,
        'real_name': hero.real_name,
        'secret_identity': hero.secret_identity,
    }
    t = get_template('superheroes/hero_basic.html')
    page = t.render(data)
    return HttpResponse(page)

def hero_easy_way(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero_name': hero.name,
        'real_name': hero.real_name,
        'secret_identity': hero.secret_identity,
    }
    return render(request, 'superheroes/hero_basic.html', context=data)

def hero_lookups(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
    }
    return render(request, 'superheroes/hero_lookups.html', data)

def hero_filters(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
    }
    return render(request, 'superheroes/hero_filters.html', data)

def hero_tags(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
    }
    return render(request, 'superheroes/hero_tags.html', data)

def hero_details(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
    }
    return render(request, 'superheroes/hero_details.html', data)

def hero_escape(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
        'html_fragment': '<i>Some HTML</i>'
    }
    return render(request, 'superheroes/hero_escape.html', data)

def hero_urls(request):
    context = {
        'title': 'Superheroes',
        'superheroes': Superhero.objects.all()
    }
    return render(request, 'superheroes/hero_urls.html', context)

def hero_static(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
        'image_name': hero.name.lower().replace(' ', '_')
    }
    return render(request, 'superheroes/hero_static.html', data)
