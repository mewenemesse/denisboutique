from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    image = models.ImageField(upload_to='Categorie',null=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom
    
class Produits(models.Model):
    libelle = models.CharField(max_length=100)
    prix = models.IntegerField()
    quantite = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.libelle

# class Produit(models.Model):
#     nom = models.CharField(max_length=200)
#     categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
#     prix = models.DecimalField(max_digits=10, decimal_places=2)
#     quantite = models.IntegerField(default=0)
#     date_ajout = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.nom

# class Vente(models.Model):
#     date = models.DateTimeField(default=timezone.now)
#     montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def calculer_montant(self, produits):
#         self.montant_total = sum(p.prix for p in produits)
#         self.save()

# class LigneVente(models.Model):
#     vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
#     produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     quantite = models.IntegerField()
#     prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
