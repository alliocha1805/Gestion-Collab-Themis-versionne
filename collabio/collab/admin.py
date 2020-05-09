from django.contrib import admin

# Register your models here.
from .models import competences, familleCompetences, outils, familleOutils, collaborateurs, experiences, domaine, client, projet

admin.site.register(competences)
admin.site.register(familleCompetences)
admin.site.register(outils)
admin.site.register(familleOutils)
admin.site.register(collaborateurs)
class ExpeAdmin(admin.ModelAdmin):
    search_fields = ['collaborateurMission__nomCollaborateur','collaborateurMission__prenomCollaborateur']
admin.site.register(experiences, ExpeAdmin)
admin.site.register(projet)
admin.site.register(domaine)
admin.site.register(client)