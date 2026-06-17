from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('import-excel/', views.import_excel_page, name='import_excel'),

    # Etudiant
    path('recherche/', views.recherche_livre, name='recherche'),
    path('emprunts/', views.mes_emprunts, name='emprunts'),
    path('fiche/', views.fiche_etudiant, name='fiche'),
    path('changer-mot-de-passe/', views.changer_mot_de_passe, name='changer_mot_de_passe'),


    # Bibliothecaire
    path('gestion-livres/', views.gestion_livres, name='gestion_livres'),
    path('gestion-membres/', views.gestion_membres, name='gestion_membres'),
    path('gestion-emprunts/', views.gestion_emprunts, name='gestion_emprunts'),
    path('import-livres/', views.import_livres_excel, name='import_livres'),
    path('notifications/', views.retards_page, name='notifications'),
    path('notifier/', views.notifications_retard, name='notifier'),
    path('import-etudiants/', views.import_etudiants_excel, name='import_etudiants'),

    # Administrateur
    path('dashboard/', views.dashboard, name='dashboard'),
    path('comptes/', views.gestion_comptes, name='comptes'),
    path('rapport/', views.rapport, name='rapport'),
    path('rapport-pdf/<int:rapport_id>/', views.rapport_pdf, name='rapport_pdf'),
]