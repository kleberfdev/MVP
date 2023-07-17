from django import forms
from .models import User, Item

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

class ItemForm(forms.ModelForm):
    quantidade = forms.IntegerField()  # Adicione o campo quantidade aqui

    class Meta:
        model = Item
        fields = ('name', 'description', 'quantidade')  # Adicione 'quantidade' aqui
