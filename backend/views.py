from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib import messages
from backend.models import Categorie,Produits
from . forms import *


# Create your views here.
def Accueil(request):
   return render(request , "index.html" ) 


def Dashboard(request):
    return render(request, 'dashboard.html')


def categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST,request.FILES)
        if form.is_valid():
            cat = form.save()
            return redirect('categories')
        else:
            print(form.errors)
            
    else: 
        form =CategorieForm()
    return render(request, 'categorie.html', {'form': form})


def categories(request):
    categories = Categorie.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def modifyCategorie(request,id):
    categorie= Categorie.objects.get(id=id)
    form = CategorieForm(instance=categorie)
    if request.method == 'POST':
        form = CategorieForm(request.POST,instance=categorie )
        if form.is_valid():
            form.save()
        return redirect ('categories')

    return render (request, 'modif.html', {'form':form, 'Categorie':Categorie})


def deleteCategorie(request,id):
    categorie = Categorie.objects.get(id=id)
    categorie.delete()
    return redirect ('categories')
    




def produit(request):
    if request.method == 'POST':
        form = ProduitsForm(request.POST)
        if form.is_valid():
            cat = form.save()
            return redirect('produits')
        else:
            print(form.errors)
            
    else: 
        form =ProduitsForm()
    return render(request, 'produit.html', {'form': form})


def produits(request):
    produits = Produits.objects.all()
    return render(request, 'produits.html', {'produits': produits})







# def accueil(request):
#     return render(request, 'gestion/accueil.html')

# def liste_produits(request):
#     produits = Produit.objects.all()
#     return render(request, 'gestion/produits.html', {'produits': produits})

# def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit ajouté avec succès!')
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'gestion/ajouter_produit.html', {'form': form})

# def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit modifié avec succès!')
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'gestion/modifier_produit.html', {'form': form})

# def supprimer_produit(request, pk):
#     produit = get_object_or_404(Produit, pk=pk)
#     produit.delete()
#     messages.success(request, 'Produit supprimé avec succès!')
#     return redirect('liste_produits')

# def rechercher_produit(request):
#     query = request.GET.get('q')
#     produits = Produit.objects.filter(nom__icontains=query) if query else []
#     return render(request, 'gestion/recherche.html', {'produits': produits, 'query': query})

# def creer_vente(request):
#     produits = Produit.objects.filter(quantite__gt=0)
#     if request.method == 'POST':
#         # Logique de création de vente
#         vente = Vente.objects.create()
#         # Traitement des produits vendus
#         return redirect('detail_vente', pk=vente.pk)
#     return render(request, 'gestion/creer_vente.html', {'produits': produits})

# def tableau_bord(request):
#     # Statistiques de vente
#     stats = {
#         'total_produits': Produit.objects.count(),
#         'total_categories': Categorie.objects.count(),
#         'total_ventes': Vente.objects.count(),
#         'chiffre_affaires': Vente.objects.aggregate(total=Sum('montant_total'))['total'] or 0,
#         'produits_rupture': Produit.objects.filter(quantite=0).count(),
#     }
#     return render(request, 'gestion/dashboard.html', {'stats': stats})
