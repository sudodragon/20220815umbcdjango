# Generated by Django 3.1.2 on 2020-11-01 20:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID of this city', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='City name', max_length=64)),
                ('admindiv', models.CharField(help_text='Administrative Division (State/Province etc.)', max_length=128, null=True)),
                ('country', models.CharField(default='US', help_text='Country code', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'cities',
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID of this contact', primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First name', max_length=32)),
                ('last_name', models.CharField(help_text='Last name', max_length=32)),
                ('street_address', models.CharField(help_text='Street address', max_length=32, null=True)),
                ('postcode', models.CharField(help_text='Postal code (Zip, etc)', max_length=16, null=True)),
                ('dob', models.DateField(help_text='Date of birth', null=True)),
                ('city', models.ForeignKey(help_text='City for this contact', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='contacts_core.city')),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
    ]