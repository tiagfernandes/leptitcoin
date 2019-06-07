from django.db import models
from django.utils import timezone


class Annonces(models.Model):
    titre = models.CharField(max_length=100)
    vendeur = models.CharField(max_length=42)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    contenu = models.TextField(null=True)
    prix = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = "annonce"
        ordering = ['date']

    def __str__(self):
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
