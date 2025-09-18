from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}".strip()

class Manga(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='mangas')
    date_publication = models.DateField()
    genre = models.CharField(max_length=100)
    resume = models.TextField(blank=True)

    def __str__(self):
        return self.titre
