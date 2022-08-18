from django.db import models

class Genre(models.Model):
    """
    Genre of band. Each band has one genre.
    """
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length=32, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    members = models.ManyToManyField(Artist, through='BandMember')

    def __str__(self):
        return self.name

class Album(models.Model):
    album_name = models.CharField(max_length=512, unique=True)
    release_year = models.PositiveSmallIntegerField(null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name

class BandMember(models.Model):
    member = models.ForeignKey(Artist, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    is_current_or_last = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member}/{self.band}"