from django.db import models


class President(models.Model):
    termnum = models.AutoField(blank=True, primary_key=True)
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

    def __str__(self):
        return f"{self.termnum}: {self.firstname} {self.lastname}"
