# Generated by Django 2.2.5 on 2020-05-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0003_auto_20200509_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborateurs',
            name='codePostal',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='mail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='telephone',
            field=models.TextField(default=''),
        ),
    ]