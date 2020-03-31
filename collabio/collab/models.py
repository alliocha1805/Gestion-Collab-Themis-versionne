from django.db import models
from django.forms import ModelForm

#Clients
class domaine(models.Model):
    nomDomaine = models.CharField(max_length=300)
    def __str__(self):
        return self.nomDomaine

class client(models.Model):
    nomClient = models.CharField(max_length=250)
    domaineClient = models.ForeignKey(domaine, on_delete=models.CASCADE)
    logoClient = models.ImageField(upload_to='collab/static/collab', blank=True, null=True)
    def __str__(self):
        return self.nomClient

#Outils 
class familleOutils(models.Model):
    nomFamilleOutils = models.CharField(max_length=250)
    def __str__(self):
        return self.nomFamilleOutils

class outils(models.Model):
    nomOutil = models.CharField(max_length=250)
    famille = models.ForeignKey(familleOutils, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomOutil

#Compétences
class familleCompetences(models.Model):
    nomFamilleCompetence = models.CharField(max_length=250)
    def __str__(self):
        return self.nomFamilleCompetence

class competences(models.Model):
    nomCompetence = models.CharField(max_length=250)
    famille = models.ForeignKey(familleCompetences, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomCompetence



#Collaborateur
class collaborateurs(models.Model):
    nomCollaborateur = models.CharField(max_length=200)
    prenomCollaborateur = models.CharField(max_length=200)
    titreCollaborateur = models.CharField(max_length=200)
    texteIntroductifCv = models.TextField(default='')
    nbAnneeExperience = models.IntegerField()
    listeCompetencesCles = models.ManyToManyField(competences)
    formation = models.TextField()
    parcours = models.TextField()
    methodologie = models.TextField()
    langues = models.TextField()
    outilsCollaborateur = models.ManyToManyField(outils)
    estEnIntercontrat = models.BooleanField(default=False)
    def __str__(self):
        return self.nomCollaborateur

#Experiences
class experiences(models.Model):
    nomMission = models.CharField(max_length=300)
    niveauIntervention = models.CharField(max_length=300, default="")
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    dateDebut = models.DateField('date de début de mission')
    dateFin = models.DateField('date de fin de mission', blank=True, null=True)
    nbJourHomme = models.IntegerField()
    contexteMission = models.TextField()
    descriptifMission = models.TextField()
    environnementMission =  models.TextField()
    collaborateurMission = models.ForeignKey(collaborateurs, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.nomMission