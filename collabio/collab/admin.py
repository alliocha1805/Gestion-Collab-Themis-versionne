from django.contrib import admin

# Register your models here.
from .models import competences, familleCompetences, outils, familleOutils, collaborateurs, experiences, domaine, client

admin.site.register(competences)
admin.site.register(familleCompetences)
admin.site.register(outils)
admin.site.register(familleOutils)
admin.site.register(collaborateurs)
admin.site.register(experiences)
admin.site.register(domaine)
admin.site.register(client)