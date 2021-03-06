# Generated by Django 2.2.5 on 2020-02-04 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomClient', models.CharField(max_length=250)),
                ('logoClient', models.ImageField(blank=True, null=True, upload_to='collab/static/collab')),
            ],
        ),
        migrations.CreateModel(
            name='collaborateurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCollaborateur', models.CharField(max_length=200)),
                ('prenomCollaborateur', models.CharField(max_length=200)),
                ('titreCollaborateur', models.CharField(max_length=200)),
                ('texteIntroductifCv', models.TextField(default='')),
                ('nbAnneeExperience', models.IntegerField()),
                ('formation', models.TextField()),
                ('parcours', models.TextField()),
                ('methodologie', models.TextField()),
                ('langues', models.TextField()),
                ('estEnIntercontrat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='domaine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomDomaine', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='familleCompetences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFamilleCompetence', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='familleOutils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFamilleOutils', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='outils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomOutil', models.CharField(max_length=250)),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collab.familleOutils')),
            ],
        ),
        migrations.CreateModel(
            name='experiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMission', models.CharField(max_length=300)),
                ('niveauIntervention', models.CharField(default='', max_length=300)),
                ('dateDebut', models.DateField(verbose_name='date de début de mission')),
                ('dateFin', models.DateField(blank=True, null=True, verbose_name='date de fin de mission')),
                ('nbJourHomme', models.IntegerField()),
                ('contexteMission', models.TextField()),
                ('descriptifMission', models.TextField()),
                ('environnementMission', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collab.client')),
                ('collaborateurMission', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='collab.collaborateurs')),
            ],
        ),
        migrations.CreateModel(
            name='competences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCompetence', models.CharField(max_length=250)),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collab.familleCompetences')),
            ],
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='listeCompetencesCles',
            field=models.ManyToManyField(to='collab.competences'),
        ),
        migrations.AddField(
            model_name='collaborateurs',
            name='outilsCollaborateur',
            field=models.ManyToManyField(to='collab.outils'),
        ),
        migrations.AddField(
            model_name='client',
            name='domaineClient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collab.domaine'),
        ),
    ]
