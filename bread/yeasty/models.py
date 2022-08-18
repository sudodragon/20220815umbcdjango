from django.db import models

class ExtraLoaf(models.Models):
    extra_data = models.BinaryField(max_length=1024)

# Create your models here.
class Loaf(models.Model):
    loaf_name = models.CharField(max_length=64)
    rising_time = models.IntegerField()
    band_start_year = models.IntegerField()
    other_data = models.OnetoOneField(ExtraLoaf)

    class Meta:
        db_table = "loaves"

    def __str__(self):
        return self.loaf_name

