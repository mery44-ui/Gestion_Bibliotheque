# ─── Exceptions personnalisées ────────────────────────────────

class LoginIncorrectException(Exception):
    """Login ou mot de passe incorrect."""
    pass

class CompteBloquéException(Exception):
    """Compte bloqué après 3 tentatives échouées."""
    pass

class CompteInactifException(Exception):
    """Compte désactivé par l'administrateur."""
    pass

class LivreIndisponibleException(Exception):
    """Livre déjà emprunté."""
    pass

class LivreIntrouvableException(Exception):
    """Livre inexistant dans la BDD."""
    pass

class MembreIntrouvableException(Exception):
    """Étudiant inexistant dans la BDD."""
    pass

class EmpruntIntrouvableException(Exception):
    """Emprunt inexistant ou déjà rendu."""
    pass

class EmpruntEnCoursException(Exception):
    """Suppression impossible — membre a des emprunts en cours."""
    pass

class DoublonException(Exception):
    """Élément déjà existant dans la BDD."""
    pass

class FichierExcelInvalideException(Exception):
    """Fichier Excel manquant, vide ou colonnes incorrectes."""
    pass

class MotDePasseInvalideException(Exception):
    """Mot de passe actuel incorrect."""
    pass