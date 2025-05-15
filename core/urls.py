from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('membre/inscription/', views.register, name='register'),
    path(
    'membre/login/',
    auth_views.LoginView.as_view(template_name='core/login.html'),
    name='login'
    ),

    path('membre/logout/', auth_views.LogoutView.as_view(next_page='accueil'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/proposer/', views.proposer_article, name='proposer_article'),
    path('membre/logout/', auth_views.LogoutView.as_view(next_page='accueil'), name='logout'),
    path('dashboard/article/<int:pk>/', views.article_apercu, name='article_apercu'),
    path('dashboard/article/<int:pk>/', views.article_apercu, name='article_apercu'),
    path('dashboard/article/<int:pk>/modifier/', views.modifier_article, name='modifier_article'),



]   






