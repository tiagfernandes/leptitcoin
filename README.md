# LePtitCoin
FERNANDES Tiago

Projet exam Django Hitema 2019

Site de vente avec Django

## Installer les paquets

`pip install django-crispy-forms`

`pip install django-debug-toolbar`

`pip install pillow`


##

La page principale regroupe la totalité des annonces en base de données.
Il est possible de pouvoir les filtrer par catégorie.

On peut créer un article, le lien pour accéder à la page est dans le menu en haut à droite.

Il est possible d'afficher une annonce en particulier dans son détail. 
Une fois sur la page de détail il est possible de pouvoir cliquer sur un bouton pour modifier l'annonce.
Un autre bouton permet de pouvoir contacter le vendeur.

Une fois sur la page de modification on trouve les informations du vendeur (tel, mail).
On peut directement envoyer un mail depuis cette page (ne fonctionne pas puisqu'il n'y a pas de serveur de mail).

Pour la modification de l'annonce, il est possible depuis cette page de la supprimer, 
une confirmation sera alors demandée à l'utilisateur.