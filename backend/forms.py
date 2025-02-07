from django .forms import ModelForm
from backend.models import Categorie, Produits


class CategorieForm(ModelForm):
    class Meta:
        model=Categorie
        fields = "__all__"
        
        
class ProduitsForm(ModelForm):
    class Meta:
        model=Produits
        fields = "__all__"