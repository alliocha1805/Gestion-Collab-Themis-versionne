# Generated by Django 2.2.5 on 2020-05-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0002_projet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='experiencesLiees',
            field=models.ManyToManyField(to='collab.experiences'),
        ),
    ]