# Librairie Mangas 📚

Ce projet est une application Django permettant de gérer une bibliothèque de mangas.

## Fonctionnalités

- Liste des mangas avec titre, auteur, date de publication, genre et résumé
- Gestion des auteurs
- Interface d’administration Django

## Structure du projet

- `librairie_mangas/` : dossier principal du projet Django
  - `manage.py` : utilitaire de gestion du projet
  - `librairie_mangas/` : configuration du projet (settings, urls, wsgi, asgi)
  - `mangas/` : application principale
    - `models.py` : modèles `Auteur` et `Manga`
    - `views.py` : vue pour afficher la liste des mangas
    - `urls.py` : routes de l’application
    - `admin.py` : enregistrement des modèles dans l’admin
    - `templates/mangas/liste.html` : template pour la liste des mangas

## Installation

1. Cloner le dépôt
2. Installer les dépendances :
    ```sh
    pip install django
    ```
3. Appliquer les migrations :
    ```sh
    python manage.py migrate
    ```
4. Créer un superutilisateur (optionnel) :
    ```sh
    python manage.py createsuperuser
    ```
5. Lancer le serveur de développement :
    ```sh
    python manage.py runserver
    ```

## Utilisation

- Accéder à la liste des mangas sur la page d’accueil (`/`)
- Accéder à l’interface d’administration sur `/admin/`

## Modèles

- [`mangas.models.Auteur`](mangas/models.py) : nom, prénom
- [`mangas.models.Manga`](mangas/models.py) : titre, auteur, date_publication, genre, résumé

## Tests

Pour lancer les tests :
```sh
python manage.py test
```

## Licence

Projet éducatif, libre d’utilisation.