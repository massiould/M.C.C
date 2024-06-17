from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'})
        self.fields['first_name'].widget = forms.TextInput(attrs={ 'class': 'form-control','placeholder': 'Nom'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmation du mot de passe'})

class CheckForm(forms.Form):
    Siren = forms.CharField()
    Barreau = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Ancien mot de passe', widget=forms.PasswordInput)
    new_password = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirmer le nouveau mot de passe', widget=forms.PasswordInput)

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email")

