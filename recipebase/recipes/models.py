from django.db import models

class Unit(models.Model):
    unit_name = models.CharField(max_length=32)

    def __str__(self):
        return self.unit_name

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=128, unique=True)
    amount = models.FloatField(null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ingredient_name

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=128, unique=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.recipe_name
