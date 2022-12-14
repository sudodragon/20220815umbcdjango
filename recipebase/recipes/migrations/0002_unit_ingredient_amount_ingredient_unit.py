# Generated by Django 4.1 on 2022-08-15 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.unit'),
        ),
    ]
