# Generated by Django 3.2.7 on 2021-09-18 14:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024)),
                ('lastname', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('DNI', 'Dni'), ('PASAPORTE', 'Passport'), ('LC', 'Lc')], default='DNI', max_length=256)),
                ('number', models.CharField(max_length=256)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.person')),
            ],
        ),
    ]
