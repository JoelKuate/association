from django import forms
from .models import ContactMessage
from .models import Article 

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'sujet', 'message']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'slug', 'contenu', 'image']
