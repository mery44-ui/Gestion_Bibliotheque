## 📚 Bibliothèque Universitaire — Gestion Bibliothèque

Application web de gestion d'une bibliothèque universitaire, développée avec **Django** dans le cadre d'un projet académique en équipe.


## 👥 Équipe

| Étudiante | Rôle | Branche |
|-----------|------|---------|
| Asmae | Configuration Django, modèles, base de données |
| Rihab | Vues (views.py), logique métier, URLs |
| Meryam| Templates HTML, design, frontend Bootstrap | `meryam-design` |

---

## 🗂️ Structure du projet

```
Gestion_Bibliotheque/
│
├── bibliotheque/          # Configuration Django
│   ├── settings.py        # Paramètres du projet
│   ├── urls.py            # URLs principales
│   └── wsgi.py
│
├── core/                  # Application principale
│   ├── templates/         # Templates HTML (Étudiante 3)
│   │   ├── base.html          ← Design général, navbar, Bootstrap
│   │   ├── recherche.html     ← Page recherche de livres
│   │   ├── dashboard.html     ← Tableau de bord statistiques
│   │   └── mes_emprunts.html  ← Liste des emprunts d'un étudiant
│   ├── views.py           # Vues (Étudiante 2)
│   ├── models.py          # Modèles base de données (Étudiante 1)
│   └── urls.py            # URLs de l'application
│
└── manage.py
```

## ⚙️ Installation et lancement

### Prérequis
- Python 3.14+
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/mery44-ui/Gestion_Bibliotheque.git
cd Gestion_Bibliotheque

# 2. Installer Django
py -3.14 -m pip install django

# 3. Lancer le serveur
py -3.14 manage.py runserver
```

### Accéder à l'application

| Page | URL |
|------|-----|
| Tableau de bord | http://127.0.0.1:8000/dashboard/ |
| Recherche de livres | http://127.0.0.1:8000/recherche/ |
| Mes emprunts | http://127.0.0.1:8000/emprunts/ |

---

## 🎨 Frontend — Templates HTML (Étudiante 3)

Les templates utilisent le **Django Template Language** avec **Bootstrap 5**.

### base.html
Template parent dont héritent toutes les pages. Contient :
- La navbar avec le nom de l'application
- L'intégration de Bootstrap 5 (CDN)
- Le style général (couleurs, cartes, boutons)
- Le bloc `{% block content %}` remplacé par chaque page

### recherche.html
- Formulaire de recherche par titre ou auteur
- Tableau de résultats avec badge Disponible / Emprunté
- Hérite de `base.html` via `{% extends 'base.html' %}`

### dashboard.html
- Cartes statistiques : total livres, disponibles, emprunts en cours, retards
- Cartes membres : actifs, nouveaux ce mois, retours ce mois
- Hérite de `base.html`

### mes_emprunts.html
- Tableau des emprunts personnels
- Badge vert (En cours) ou rouge (Retard X jours)
- Hérite de `base.html`

---

## 🔗 Fonctionnement Django Template Language

```
views.py  →  envoie les données  →  template HTML  →  navigateur
```

Exemple :
```python
# views.py envoie :
return render(request, 'dashboard.html', {'data': data})

# dashboard.html affiche :
{{ data.total_livres }}
```

---

## 📋 Technologies utilisées

- **Django 6.0.5** — Framework web Python
- **Bootstrap 5.3** — Framework CSS responsive
- **Python 3.14** — Langage de programmation
- **Git / GitHub** — Contrôle de version et collaboration

---

## 🌿 Branches Git

```bash
# Voir toutes les branches
git branch -a

# Changer de branche
git checkout meryam-design
```
