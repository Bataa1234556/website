from django import forms
from .models import Good

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['name', 'description', 'price', 'image', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
