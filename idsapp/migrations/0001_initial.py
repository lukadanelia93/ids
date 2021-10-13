# Generated by Django 3.2.7 on 2021-10-13 13:42

import datetime
import django.core.validators
from django.db import migrations, models
import idsapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idcards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poto', models.ImageField(default='', upload_to='static')),
                ('cardno', models.CharField(default='', max_length=100)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lasttname', models.CharField(default='', max_length=100)),
                ('cit', models.CharField(default='', max_length=100)),
                ('sex', models.CharField(choices=[('ma', 'Male'), ('fe', 'Female')], max_length=20)),
                ('personalno', models.CharField(default='', max_length=11, validators=[idsapp.models.only_int, django.core.validators.MinLengthValidator(11)])),
                ('dateofbirth', models.DateField(default=datetime.date.today)),
                ('dateofexpiry', models.DateField(default=datetime.date.today)),
                ('signature', models.CharField(default='', max_length=100)),
                ('placeofbirth', models.CharField(default='', max_length=100)),
                ('dateofissue', models.DateField(default=datetime.date.today)),
                ('issuingauthority', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'idcards',
            },
        ),
    ]