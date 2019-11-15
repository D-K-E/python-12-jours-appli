##############
Spécification
##############

Auteur: Kaan Eraslan


Le vocabulaire employé dans ce document conforme au `RFC 2116 <https://tools.ietf.org/rfc/rfc2119.txt>`_

Aperçu
-------

Celui-ci est un document de spéficication technique d'une application au but éducatif
conçu pour la série de `python dans 12 jours <https://github.com/D-K-E/python-12-jours>`_.
Le programme regroupe les concepts qu'on vient de voir dans la série.

Réquisitions
-------------

Il a deux principales fonctionalités:

- Affichage et modification des fichiers textes.
- Filtrage des chemins en fonction des mots clés.

Il a aussi un interface graphique avec 5 composants:

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

Le format de texte accepté est texte brut dont l'extension est :code:`.txt`. 
Le programme reçoit le chemin d'un fichier :code:`.txt`, montre son contenu
dans la zone d'affichage de contenu. On permet l'utilisateur de modifier 
le contenu dans la zone.

Filtrage des Chemins
----------------------

En fonction d'un mot clé saisi par l'utilisateur, le programme filtre 
les chemins qui renvoient aux textes qui ne contiennent pas le mot clé. 
Il, donc garde uniquement les chemins de texte qui contiennent le mot clé.
Les chemins gardés sont affichés dans la zone d'affichage des chemins.
