def rechercher_etudiant_etudiants(etudiants, nom):
    """Retourne les étudiants dont le nom contient le texte recherché."""
    return [e for e in etudiants if nom.lower() in e.lower()]
