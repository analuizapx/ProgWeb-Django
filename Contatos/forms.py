from django import forms
from Contatos.models import Psicologo

class ContatoModel2Form(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = '__all__' 