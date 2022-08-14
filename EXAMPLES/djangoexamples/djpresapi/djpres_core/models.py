
from django.db import models


class President(models.Model):
    lastname = models.CharField(max_length=32, blank=True, null=True)
    firstname = models.CharField(max_length=64, blank=True, null=True)
    termstart = models.DateField(blank=True, null=True)
    termend = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=128, blank=True, null=True)
    birthstate = models.CharField(max_length=32, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    party = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'presidents'
