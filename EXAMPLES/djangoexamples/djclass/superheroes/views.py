from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Superhero, City

def home(request):
    data = {
        "message": "whatever....",
    }
    return render(request, 'superheroes/home.html', data)

class BaseHomeView(TemplateView):
    template_name = 'superheroes/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.data)
        return context

class HomeView(BaseHomeView):
    data = {'message': 'Welcome to the superheroes app for class-based views',
}
class OtherView(BaseHomeView):
    data = {'message': "This is the other view"}

class HeroListView(ListView):
    model = Superhero

class HeroDetailView(DetailView):
    model = Superhero

class HeroListViewPlus(ListView):
    model = Superhero
    context_object_name = 'heroes'
    template_name = 'superheroes/superhero_list_plus.html'
    # queryset = Superhero.objects.filter(powers__name__icontains="fly")


class HeroDetailViewPlus(DetailView):
    model = Superhero
    context_object_name = 'hero'
    template_name = 'superheroes/superhero_detail_plus.html'

class HeroCreateView(CreateView):
    model = Superhero
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')

class CityCreateView(CreateView):
    model = City
    fields = ['name']
    success_url = reverse_lazy('superheroes:success')

class HeroUpdateView(UpdateView):
    model = Superhero
    # template = "hero_update.html"
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')

class HeroDeleteView(DeleteView):
    model = Superhero
    success_url = "/"
#    success_url = reverse_lazy('superheroes:success')

class SuccessView(TemplateView):
    template_name = 'superheroes/success.html'
