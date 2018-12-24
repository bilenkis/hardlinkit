from django import forms
from .models import dirTree


class NameForm(forms.ModelForm):
    class Meta:
        model = dirTree
        fields = ('name', 'path',)
