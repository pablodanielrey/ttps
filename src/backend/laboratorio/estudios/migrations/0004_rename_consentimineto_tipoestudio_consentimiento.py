# Generated by Django 3.2.8 on 2021-10-21 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudios', '0003_estudio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoestudio',
            old_name='consentimineto',
            new_name='consentimiento',
        ),
    ]
