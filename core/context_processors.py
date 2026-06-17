from datetime import date
from core.models import Emprunt, Etudiant

def notifications_context(request):
    if 'user_id' not in request.session:
        return {}
        
    role = request.session.get('role')
    user_id = request.session.get('user_id')
    aujourd_hui = date.today()
    
    notifications = []
    
    if role in ['administrateur', 'bibliothecaire']:
        # Retards globaux pour le personnel
        retards = Emprunt.objects.filter(
            rendu=False,
            date_retour_prevue__lt=aujourd_hui
        ).select_related('etudiant', 'livre').order_by('date_retour_prevue')
        
        for e in retards:
            jours = (aujourd_hui - e.date_retour_prevue).days
            notifications.append({
                'id': e.id,
                'titre': f"{e.etudiant.prenom} {e.etudiant.nom}",
                'description': f"Livre : {e.livre.titre}",
                'url': "/notifications/",
                'date': e.date_retour_prevue.strftime('%d/%m/%Y'),
                'jours': jours,
                'type': 'retard_general'
            })
            
    elif role == 'etudiant':
        # Retards propres à l'étudiant connecté
        try:
            etudiant = Etudiant.objects.get(utilisateur__id=user_id)
            retards = Emprunt.objects.filter(
                etudiant=etudiant,
                rendu=False,
                date_retour_prevue__lt=aujourd_hui
            ).select_related('livre').order_by('date_retour_prevue')
            
            for e in retards:
                jours = (aujourd_hui - e.date_retour_prevue).days
                desc = f"Livre : {e.livre.titre} ({jours}j de retard)"
                if e.notif_envoyee:
                    desc += " — Rappel envoyé"
                notifications.append({
                    'id': e.id,
                    'titre': "Retard de retour",
                    'description': desc,
                    'url': "/emprunts/",
                    'date': e.date_retour_prevue.strftime('%d/%m/%Y'),
                    'jours': jours,
                    'type': 'retard_etudiant'
                })
        except Etudiant.DoesNotExist:
            pass
            
    return {
        'global_notifications': notifications,
        'global_notif_count': len(notifications)
    }
