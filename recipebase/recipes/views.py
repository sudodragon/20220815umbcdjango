from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render
from recipes.models import *

def home(request):
    return HttpResponse("Welcome to recipes. Try /steak")

# Create your views here.
def steak(request):
    recipe = Recipe.objects.get(id=1)  # .get(recipe_name="Grilled Steak")
    ingredients = [i.ingredient_name for i in recipe.ingredients.all()]
    ingredient_list = ', '.join(ingredients)
    return HttpResponse(f"Ingredients for {recipe.recipe_name} are {ingredient_list}")




# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to Recipes")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Recipes" }
#     return render(request, 'recipes/home.html', context)
