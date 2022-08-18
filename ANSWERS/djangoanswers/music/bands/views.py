from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse
from .models import Band, Genre, Album, Artist, BandMember

# home page
def home(request):
    context = {'message': "Welcome to the Bands app"}
    return render(request, 'bands/home.html', context)

def create(request):
    return render(request, 'bands/create.html')

def success(request):
    return render(request, 'bands/success.html')

# band pages
class BandList(ListView):
    model = Band

class BandDetails(DetailView):
    model = Band

class CreateBase(CreateView):
    template_name = "bands/common_form.html"
    data = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.data)
        return context

    def get_success_url(self, **kwargs):
        # model_name = self.model.__name__.lower()
        # return reverse(f'bands:{model_name}create')
        return reverse('bands:success')

class BandCreate(CreateBase):
    model = Band
    data = {"heading": "Add a Band", "submit_label": "add band"}
    fields = ['name', 'genre', 'members']


# album pages
class AlbumList(ListView):
    model = Album

class AlbumDetails(DetailView):
    model = Album

class AlbumCreate(CreateBase):
    model = Album
    data = {"heading": "Create an album", "submit_label": "create album"}
    fields = ['album_name', 'release_year', 'band']

# artist pages
class ArtistList(ListView):
    model = Artist

class ArtistDetails(DetailView):
    model = Artist

class ArtistCreate(CreateBase):
    model = Artist
    data = {"heading": "Create an artist", "submit_label": "create artist"}
    fields = ['name']

# bandmember pages
class BandMemberList(ListView):
    model = BandMember

class BandMemberDetails(DetailView):
    model = BandMember

class BandMemberCreate(CreateBase):
    model = BandMember
    data = {"heading": "Create a band member", "submit_label":  "create band member"}
    fields = ['member', 'is_current_or_last', 'band']

# genre pages
class GenreList(ListView):
    model = Genre

class GenreDetails(DetailView):
    model = Genre

class GenreCreate(CreateBase):
    model = Genre
    data = {"heading": "Create a genre", "submit_label": "create genre"}
    fields = ['name']
