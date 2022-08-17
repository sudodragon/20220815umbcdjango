from django.db import models
import logging

logging.basicConfig(
    filename='superheroes.log',
    level=logging.INFO,
)

class SuperheroManager(models.Manager):
    def get_fliers(self):
        return self.filter(powers__name__icontains="fly")

class Power(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=32)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

class Superhero(models.Model):
    name = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32, default="John Doe")
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)

    objects = SuperheroManager()

    def __str__(self):
        return self.name
    # Superhero._meta.app_label

    class Meta:
        ordering = ['secret_identity']
        # db_table = "pastafazool"
        app_label = "superheroes"
        # managed = False  # Django will not migrate changes to this table
        # verbose_name = "???"  # lady   ladys
        # verbose_name_plural = "???s"  # ladies

    def get_brief_enemies(self):
        enemies = [e.name.split()[-1] for e in self.enemies.all()]
        return '/'.join(enemies)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   # call base ('real') save method
        logging.info("Created superhero {}".format(self.name))
        # do something else here as needed

