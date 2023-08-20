# Les tests de nos différentes fonctions

# Importation des fichiers necessaires
import login
import utilisateurs
import verifier
import grille_tarifaire
import colis
import payements
import verifier


# Fonction de test pour l'inscription des utilisateurs
def test_inscription_utilisateurs():

    utilisateurs.create_table_utilisateurs() # Création de la table

    # Cas 1 : test de l'inscription d'un nouveau utilisateur
    nom_utilisateur = "donatien"
    email = "donaCO1234"
    password = "test@mail.com"
    numero = "77000000"
    # Verifier si l'insertion dans la BD a réussi
    utilisateurs.enregistrement_utilisateurs(nom_utilisateur, email, password, numero) is True

    # Cas 1 : test de l'inscription d'un utilisateur existant
    # Verifier si l'insertion dans la BD a échoué
    utilisateurs.enregistrement_utilisateurs(nom_utilisateur, email, password, numero) is None


# Fonction de test pour la connexion des utilisateurs
def test_connexion():
    # Cas 1 : Test pour une connexion réussie
    nom_utilisateur = "donatien"
    password = "donaCO1234"
    login.login(nom_utilisateur, password) is True

    # Cas 2 : Test pour une connexion échouée
    login.login(nom_utilisateur, password) is None


# Fonction de test pour les dévis
def test_devis():
    # Cas : Test pour des valeurs correctes
    poids = 5
    distance = 7.6
    oracle = 10100
    assert grille_tarifaire.devis(poids, distance) == oracle


# Fonction de test pour les colis
def test_colis():

    colis.create_table_colis()

    # Cas 1 : Test pour une insertion réussie d'un colis
    nom_client = "donatien"
    adresse = "Ouagadougou"
    poids_colis = "7kg"
    numero_destinataire = "64000000"
    commentaire = "colis"
    colis.enregistrement_colis(nom_client, adresse, poids_colis, numero_destinataire, commentaire) is True

    # Cas 2 : Test pour une insertion échouée d'un colis
    colis.enregistrement_colis(nom_client, adresse, poids_colis, numero_destinataire, commentaire) is None

# Fonction de test pour les payements
def test_payements():

    payements.create_table_payements()

    # Cas 1 : Test pour un payement réussi
    nom_client = "donatien"
    id_colis = "3"
    code_transaction = "F23452"
    payements.enregistrement_payement(nom_client, id_colis, code_transaction) is True

    # Cas 2 : Test pour un payement échoué
    payements.enregistrement_payement(nom_client, id_colis, code_transaction) is None

# Fonction de test pour les vérifications de saisie
def test_check_input():
    # Cas 1 : Test pour les saisies de chaine correctes
    chaine1 = "Livraison"
    verifier.check_input(chaine1)

    # Cas 2 : Test pour les saisies de chaine incorrectes
    chaine2 = "22"
    verifier.check_input(chaine2)




