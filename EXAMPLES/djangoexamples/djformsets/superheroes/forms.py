#!/usr/bin/env python
from django.forms import Form, CharField, formset_factory

class HeroForm(Form):

    hero_name = CharField(label='Hero', max_length=40)
    hero_real_name = CharField(label='Real Name', max_length=40)

HeroFormSet = formset_factory(HeroForm, extra=2)

hero_formset = HeroFormSet()



