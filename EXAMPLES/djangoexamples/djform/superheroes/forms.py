#!/usr/bin/env python
from django import forms
from .models import Superhero
from .validators import small_integer_only

class LittleIntegerField(forms.IntegerField):
    default_validators = [small_integer_only]


class DemoForm(forms.Form):
    demo_boolean = forms.BooleanField(label="Check if you love Python")
    demo_char = forms.CharField(max_length=10, strip=True)
    demo_choice = forms.ChoiceField(choices=[(1, 'A'), (2, 'B'), (3, 'C')])
    demo_date = forms.DateField(label="Date")
    demo_email = forms.EmailField(label="Electronic mail address:")
    demo_float = forms.FloatField(help_text="Please enter a floating point number")
    demo_int1 = LittleIntegerField()
    demo_int2 = LittleIntegerField()
    demo_regex = forms.RegexField(regex=r'(?i)^a[a-z]{1,5}$')
    # submit = forms

    # add clean function here...
    def clean_demo_boolean(self):
        bool = self.cleaned_data['demo_boolean']
#        raise forms.ValidationError("That is an invalid Boolean")
        return not bool

    def clean_demo_choice(self):
        choice = self.cleaned_data['demo_choice']
        value = "NONE"
        if choice == "1":
            value = "apple"
        elif choice == "2":
            value = "banana"
        elif choice == "3":
            value = "cherry"

        return value


COLORS = 'green red blue purple orange'.split()
COLOR_CHOICES = [(c.title(), c) for c in COLORS]


class HeroForm(forms.Form):

    hero_name = forms.CharField(
        label='Hero',
        max_length=40,
        # help_text="Hero name",
        widget=forms.TextInput(attrs={'placeholder': 'Hero name'})
    )
    hero_color = forms.ChoiceField(
        label="Color",
        choices=COLOR_CHOICES,
        help_text="Color for hero name"
    )


class HeroModel(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = ['name', 'real_name', 'city', 'secret_identity']
        labels = {
            'name': 'Hero Name',
            'city': 'City where they hang out',
        }


