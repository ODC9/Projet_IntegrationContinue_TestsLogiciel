# Les tests de nos différentes fonctions

# Importation des fichiers necessaires
import login
import utilisateurs
import verifier

# Fonction de test pour la création de la table des utilisateurs
def test_create_table_utilisateurs():

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

test_create_table_utilisateurs()

