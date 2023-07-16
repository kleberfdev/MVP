# accounts/forms.py

from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    # Adicione mais campos de acordo com suas necessidades e validações aqui
