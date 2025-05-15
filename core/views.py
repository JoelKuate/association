from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

def accueil(request):
    return render(request, 'core/accueil.html')


def blog_list(request):
    articles = Article.objects.filter(etat='publie').order_by('-date_publication')
    return render(request, 'core/blog_list.html', {'articles': articles})

def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, etat='publie')
    return render(request, 'core/blog_detail.html', {'article': article})

def contact(request):
    return render(request, 'core/contact.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contact.html', {
                'form': ContactForm(),  # Nouveau formulaire vide
                'message_envoye': True  # Pour afficher un message de succès
            })
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Pour l’instant, affiche les articles proposés par l’utilisateur
    articles = request.user.article_set.all().order_by('-date_creation')
    return render(request, 'core/dashboard.html', {'articles': articles})



@login_required
def proposer_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.etat = 'attente'
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'core/proposer_article.html', {'form': form})


    

@login_required
def article_apercu(request, pk):
    article = get_object_or_404(Article, pk=pk, auteur=request.user)
    return render(request, 'core/article_apercu.html', {'article': article})

@login_required
def modifier_article(request, pk):
    article = get_object_or_404(Article, pk=pk, auteur=request.user)
    if article.etat == 'publie':
        return redirect('dashboard')
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'core/modifier_article.html', {'form': form, 'article': article})
   


