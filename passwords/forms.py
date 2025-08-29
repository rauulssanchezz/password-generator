from django import forms
from .services import Complexity

class PasswordDataForm(forms.Form):
    complexity = forms.ChoiceField(
        label='Complejidad:',
        choices=[
            (item.name, item.name.capitalize()) for item in Complexity
        ]
    )

class HashPasswordForm(forms.Form):
    password = forms.CharField(label='Contraseña:')

class CheckPasswordForm(forms.Form):
    plain_password = forms.CharField(label='Contraseña sin hashear:')
    hashed_password = forms.CharField(label='Contraseña hasheada:')

class SavePasswordForm(forms.Form):
    password_name = forms.CharField(label='Nombre para la contraseña:')
    password = forms.CharField(label='Contraseña:')
