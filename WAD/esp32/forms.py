
from django import forms
from .models import ESP

class EspForm(forms.ModelForm):
    class Meta:
        model = ESP
        fields = '__all__'