from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class club_Club(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    dateCreation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom

class club_Article(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    contenu = models.TextField()
    dateCreation = models.DateTimeField(default=timezone.now)
    datePublication = models.DateTimeField(blank=True, null=True)

    def publier(self):
        self.datePublication = timezone.now()
        self.save()

    def __str__(self):
        return self.titre
