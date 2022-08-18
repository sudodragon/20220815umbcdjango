from django.contrib import admin

from .models import Band, Artist, Genre, Album, BandMember

admin.site.register(Band)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(BandMember)

