# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    ETAT_CHOICES = [
        ('brouillon', 'Brouillon'),
        ('attente', 'En attente'),
        ('publie', 'Publié'),
        ('rejete', 'Rejeté'),
    ]
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default='brouillon')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titre

class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

