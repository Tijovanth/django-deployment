from django import forms
from exampleapp.models import Registration

class RegistrationForm(forms.ModelForm):
    ConfirmEmail = forms.EmailField(label="Enter your email id again")
    Password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=Registration
        fields ="__all__"
