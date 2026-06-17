from django.contrib import admin
from .models import Utilisateur, Etudiant, Livre, Emprunt, Rapport

admin.site.register(Utilisateur)
admin.site.register(Etudiant)
admin.site.register(Livre)
admin.site.register(Emprunt)
admin.site.register(Rapport)