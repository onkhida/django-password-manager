from django import forms
from .models import UserLoginDetails

class CredentialForm(forms.ModelForm):
    class Meta:
        model = UserLoginDetails
        fields = ['site_name', 'username', 'email', 'url', 'password']



