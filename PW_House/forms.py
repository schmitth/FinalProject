from django import forms
from .models import sourceTable


class SourceForm(forms.ModelForm):
    class Meta:
        model = sourceTable
        fields = '__all__'
