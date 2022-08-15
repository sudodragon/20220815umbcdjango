from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the yeast breads app")

def baguette(request):
    return HttpResponse("Hello from Paris")


# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to yeasty")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to yeasty" }
#     return render(request, 'yeasty/home.html', context)
