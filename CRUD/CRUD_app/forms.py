from django import forms
from .models import CRUDModel

class CRUDform(forms.ModelForm):
    class Meta:
        model=CRUDModel
        fields='__all__'