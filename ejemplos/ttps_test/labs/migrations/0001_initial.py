# Generated by Django 3.2.7 on 2021-09-18 15:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0002_auto_20210918_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cost', models.IntegerField()),
                ('paid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('diagnosis', models.TextField(max_length=1024)),
                ('medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='derived_labs', to='persons.person')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='persons.person')),
            ],
        ),
        migrations.CreateModel(
            name='LabQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(choices=[('Negativo', 'Negative'), ('Positivo', 'Positive')], null=True)),
                ('sent', models.TextField(choices=[('Enviado', 'Sent'), ('Pendiente', 'Pending'), ('No Aplica', 'Doest Apply')], default='Pendiente', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='LabType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='SocialSecurityInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('paid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LabStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.TextField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.lab')),
            ],
        ),
        migrations.AddField(
            model_name='lab',
            name='quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='labs.labquote'),
        ),
        migrations.AddField(
            model_name='lab',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.labresult'),
        ),
        migrations.AddField(
            model_name='lab',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.labtype'),
        ),
    ]
