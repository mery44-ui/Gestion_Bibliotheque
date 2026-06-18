## 📚 Bibliothèque Universitaire — Gestion Bibliothèque

Application web de gestion d'une bibliothèque universitaire, développée avec **Django** dans le cadre d'un projet académique en équipe.

---

## 🚀 Comment démarrer l'application (Guide de démarrage rapide)

Voici les étapes pas à pas pour cloner, installer et lancer l'application en local :

### 1. Cloner le dépôt GitHub
Ouvrez votre terminal et clonez le projet, puis entrez dans le dossier :
```bash
git clone https://github.com/mery44-ui/Gestion_Bibliotheque.git
cd Gestion_Bibliotheque
```

### 2. Activer l'environnement virtuel (venv)
Activez l'environnement virtuel pour installer les dépendances de manière isolée :
* **Sur Windows (PowerShell) :**
  ```powershell
  python -m venv venv
  venv\Scripts\activate
  ```
* **Sur macOS / Linux :**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Installer les dépendances
Installez Django (et les autres modules si nécessaire) :
```bash
pip install django
```

### 4. Appliquer les migrations de base de données
Créez et mettez à jour votre base de données locale SQLite :
```bash
python manage.py migrate
```

### 5. Lancer le serveur de développement
Démarrez le serveur local Django :
```bash
python manage.py runserver
```

### 6. Accéder à l'application dans le navigateur
Ouvrez votre navigateur web et visitez :
👉 [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

---

## 🔄 Comment mettre à jour et pousser sur GitHub (Workflow Git)

Lorsque vous apportez des modifications locales et souhaitez les pousser sur GitHub :

1. **Vérifier le statut de vos modifications :**
   ```bash
   git status
   ```
2. **Ajouter vos fichiers modifiés :**
   ```bash
   git add .
   ```
3. **Créer un commit avec un message :**
   ```bash
   git commit -m "Description claire de vos modifications"
   ```
4. **Pousser vos commits vers GitHub :**
   * **Sur votre branche de travail (`meryam-design`) :**
     ```bash
     git push origin meryam-design
     ```
   * **Pour synchroniser et mettre à jour la branche principale (`main`) :**
     ```bash
     git checkout main
     git merge meryam-design
     git push origin main
     git checkout meryam-design
     ```

---


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
