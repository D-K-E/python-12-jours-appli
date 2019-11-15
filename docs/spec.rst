##############
Spécification
##############

Le vocabulaire employé dans ce document conforme au `RFC 2116 <https://tools.ietf.org/rfc/rfc2119.txt>`_

Le programme a trois principales fonctions:

- Affichage et modification des fichiers textes.
- Filtrage des chemins en fonction des mots clés.

L'interface graphique du programme a 5 composants:

- Zone d'affichage et modification de texte
- Un champs de saisi pour entrer les mots clés qui filtrent les chemins
- Zone d'affichage des mots clés
- Zone d'affichage des chemins
- Boutons

L'interface graphique du programme doit avoir une zone d'affichage pour une liste des chemins et une zone d'affichage
pour un contenu textuel. 

Le contenu textuel doit être modifiable. 
On doit pouvoir ajouter et supprimer des nouveaux chemins
à la liste des chemins et le zone d'affichage doit être mise au jours à chaque fois qu'on a modifié la liste des chemins.

Une champs de saisi pour filtrer les chemins en fonction de

Une vue possible de l'interface graphique est:


+------------------------------------------------+
| Titre de l'Application                         |
+==============================+=================+
|                              | - chemin 1      |
|        Zone d'Affichage      | - chemin 2      |
|        de Texte              | - chemin 3      |
|                              | - chemin 4      |
|                              | - chemin 5      |
|                              | - chemin 6      |
|                              |                 |
|                              +-----------------+
|                              |  Bouton 1       |
|                              +-----------------+
|                              |  Bouton 2       |
|                              +-----------------+
|                              |  Bouton 3       |
|                              +-----------------+
|                              | - mot clé 1     |
|                              | - mot clé 2     |
|                              | - mot clé 3     |
|                              | - mot clé 4     |
|                              |                 |
|                              +-----------------+
|                              | Champs d'Entrée |
|                              +-----------------+
|                              |  Bouton 4       |
|                              +-----------------+
|                              |  Bouton 5       |
|                              +-----------------+
|                              |  Bouton 6       |
+------------------------------+-----------------+


Affichage et Modification des Textes
-------------------------------------

Le format de texte accepté est texte brut
