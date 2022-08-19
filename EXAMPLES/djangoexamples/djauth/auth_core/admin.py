from django.contrib import admin
# Register your models here.

from .models import Person, Dog

# admin.site.register(MyModel)
admin.site.register(Person)
admin.site.register(Dog)
