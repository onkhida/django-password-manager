from django import forms

class CheckPasswordForm(forms.Form):
    password = forms.PasswordInput()