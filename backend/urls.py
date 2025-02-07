from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Accueil, name='Accueil'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('categorie/', views.categorie, name='categorie'),
    path('categories', views.categories, name='categories'),
    path('produit/', views.produit, name='produit'),
    path('produits/', views.produits, name='produits'),
    path('modifyCategorie/<int:id>/', views.modifyCategorie, name='modifyCategorie'),
    path('deleteCategorie<int:id>/', views.deleteCategorie, name='deleteCategorie'),
    # path('produits/recherche/', views.rechercher_produit, name='rechercher_produit'),
    # path('ventes/creer/', views.creer_vente, name='creer_vente'),
    # path('dashboard/', views.tableau_bord, name='tableau_bord'),
] +  static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
