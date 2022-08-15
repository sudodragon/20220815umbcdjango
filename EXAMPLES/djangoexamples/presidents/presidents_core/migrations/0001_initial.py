# Generated by Django 3.0 on 2021-05-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presidents',
            fields=[
                ('termnum', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(blank=True, max_length=32, null=True)),
                ('firstname', models.CharField(blank=True, max_length=64, null=True)),
                ('termstart', models.DateField(blank=True, null=True)),
                ('termend', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=128, null=True)),
                ('birthstate', models.CharField(blank=True, max_length=32, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('deathdate', models.DateField(blank=True, null=True)),
                ('party', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'presidents',
                'managed': True,
            },
        ),
    ]