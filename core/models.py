from django.db import models
from django.utils import timezone

class Utilisateur(models.Model):
    ROLES = [
        ('etudiant', 'Étudiant'),
        ('bibliothecaire', 'Bibliothécaire'),
        ('administrateur', 'Administrateur'),
    ]
    login        = models.CharField(max_length=50, unique=True)
    mot_de_passe = models.CharField(max_length=255)
    role         = models.CharField(max_length=20, choices=ROLES)
    actif        = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.login} ({self.role})"


class Etudiant(models.Model):
    utilisateur = models.OneToOneField(
        Utilisateur, on_delete=models.CASCADE,
        null=True, blank=True
    )
    nom       = models.CharField(max_length=100)
    prenom    = models.CharField(max_length=100)
    email     = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Livre(models.Model):
    titre      = models.CharField(max_length=200)
    auteur     = models.CharField(max_length=100)
    isbn       = models.CharField(max_length=20, blank=True)
    categorie  = models.CharField(max_length=100, blank=True)
    disponible = models.BooleanField(default=True)
    image      = models.ImageField(upload_to='couvertures/', null=True, blank=True)

    def __str__(self):
        return self.titre


class Emprunt(models.Model):
    etudiant              = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    livre                 = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt          = models.DateField(default=timezone.now)
    date_retour_prevue    = models.DateField()
    date_retour_effective = models.DateField(null=True, blank=True)
    retard                = models.FloatField(default=0)
    notif_envoyee         = models.BooleanField(default=False)
    rendu                 = models.BooleanField(default=False)

    def calculer_retard(self):
        if self.date_retour_effective and self.date_retour_prevue:
            delta = self.date_retour_effective - self.date_retour_prevue
            return max(0, delta.days)
        return 0

    def __str__(self):
        return f"{self.etudiant} → {self.livre}"


class Rapport(models.Model):
    TYPES = [
        ('emprunts', 'Rapport Emprunts'),
        ('retards',  'Rapport Retards'),
        ('membres',  'Rapport Membres'),
    ]
    date_generation = models.DateTimeField(auto_now_add=True)
    type            = models.CharField(max_length=50, choices=TYPES)
    contenu         = models.TextField(blank=True)

    def __str__(self):
        return f"Rapport {self.type} - {self.date_generation.strftime('%d/%m/%Y')}"