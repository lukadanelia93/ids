# Generated by Django 3.2.7 on 2021-10-13 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idcards',
            old_name='lasttname',
            new_name='lastname',
        ),
    ]
