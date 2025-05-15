from django.contrib import admin
from .models import Article, ContactMessage

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'etat', 'date_creation', 'date_publication')
    list_filter = ('etat', 'auteur')
    search_fields = ('titre', 'contenu')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoye', 'lu')
    list_filter = ('lu',)
    search_fields = ('nom', 'email', 'sujet', 'message')
