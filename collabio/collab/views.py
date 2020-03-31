from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from .models import competences,client,collaborateurs,outils,experiences
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Homepage
def index(request):
    template = loader.get_template('collab/index.html')
    nbConsultant = collaborateurs.objects.count()
    nbConsultantInterco = collaborateurs.objects.filter(estEnIntercontrat=True).count()
    nbConsultantEnMission = nbConsultant - nbConsultantInterco
    txInterco = round((nbConsultantInterco / nbConsultant)*100,2)
    nbCompe = competences.objects.count()
    nbClient = client.objects.count()
    #calcul du nombre de client actif (a savoir les clients avec une mission en cours a date) A REWORK CAR PAS DE PRISE EN COMPTE DE DATE
    def getClientActif():
        client_total=client.objects.all()
        count=0
        for elt in client_total:
            expes_du_client=experiences.objects.filter(client=elt)
            if expes_du_client.exists():
                pass
            else:
                count+=1
        return(count)
    nbClientActif = getClientActif()
    nbClientInactif = nbClient - nbClientActif
    txClientInactif = round((nbClientInactif / nbClient)*100,2)
    #calcul du nombre de competence moyen par consultant
    def getMoyenneCompetence():
        listeCompe=[]
        listeCollab=collaborateurs.objects.all()
        for elt in listeCollab:
            nb_compe_calcul = elt.listeCompetencesCles.count()
            listeCompe.append(nb_compe_calcul)
        moyenne=(sum(listeCompe)/len(listeCompe))
        return(moyenne)
    moyenneCompetence = getMoyenneCompetence()
    #calcul top 5 des competences - la fonction retourne la competence en position N du top
    def getTop5Competences(top):
        dicoCompetences_tempo={}
        listeCollab=collaborateurs.objects.all()
        for elt in listeCollab:
            liste_compe_test=elt.listeCompetencesCles.values("nomCompetence")
            for elt in liste_compe_test:
                compe=elt['nomCompetence']
                if compe in dicoCompetences_tempo:
                    valeur_ancienne=dicoCompetences_tempo.get("compe")
                    if valeur_ancienne == None:
                        valeur_ancienne=0
                    dicoCompetences_tempo[compe]=valeur_ancienne+1
                else:
                    dicoCompetences_tempo[compe]=1
        dicoCompetences=sorted(dicoCompetences_tempo.items(), key=lambda x: x[1], reverse=True)
        return(dicoCompetences[top])
    top1Competence=getTop5Competences(0)
    context={
    "nbConsultant":nbConsultant,
    "nbConsultantInterco":nbConsultantInterco,
    "txInterco":txInterco,
    "nbConsultantEnMission":nbConsultantEnMission,
    "nbClient":nbClient,
    "nbClientActif":nbClientActif,
    "nbClientInactif":nbClientInactif,
    "txClientInactif":txClientInactif,
    "nbCompe":nbCompe,
    "moyenneCompetence":moyenneCompetence,
    "top1Competence":top1Competence
    }
    return HttpResponse(template.render(context, request))

# Liste consultant
def liste_consultant(request):
    template = loader.get_template('collab/liste_consultant.html')
    context={}
    return HttpResponse(template.render(context, request))

#Detail consultant
#WIP

#Ajout d'un consultant
class collaborateursCreateView(CreateView):
    model = collaborateurs
    fields = ('nomCollaborateur', 'prenomCollaborateur','titreCollaborateur','texteIntroductifCv','nbAnneeExperience','listeCompetencesCles','formation','parcours','methodologie','langues','outilsCollaborateur','estEnIntercontrat')
    success_url = 'succes/'
def reussite_ajout_collaborateurs(request):
    template = loader.get_template('collab/reussite_ajout_collaborateurs.html')
    context={}
    return HttpResponse(template.render(context, request))

#Liste client
def liste_client(request):
    template = loader.get_template('collab/liste_client.html')
    context={}
    return HttpResponse(template.render(context, request))
#Ajout d'un client
class clientCreateView(CreateView):
    model = client
    fields = ('nomClient', 'domaineClient','logoClient')
    success_url = 'succes/'
def reussite_ajout_client(request):
    template = loader.get_template('collab/reussite_ajout_client.html')
    context={}
    return HttpResponse(template.render(context, request))    
#Liste compétences
def liste_competence(request):
    template = loader.get_template('collab/liste_competence.html')
    context={}
    return HttpResponse(template.render(context, request))
#Ajout d'une competence
class competencesCreateView(CreateView):
    model = competences
    fields = ('nomCompetence', 'famille')
    success_url = 'succes/'

def reussite_ajout_competence(request):
    template = loader.get_template('collab/reussite_ajout_compe.html')
    context={}
    return HttpResponse(template.render(context, request))

#Liste outil
def liste_outil(request):
    template = loader.get_template('collab/liste_outil.html')
    context={}
    return HttpResponse(template.render(context, request))

class outilsCreateView(CreateView):
    model = outils
    fields = ('nomOutil', 'famille')
    success_url = 'succes/'
def reussite_ajout_outil(request):
    template = loader.get_template('collab/reussite_ajout_outil.html')
    context={}
    return HttpResponse(template.render(context, request))