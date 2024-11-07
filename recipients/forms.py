from django import forms
from .models import Recipient

class RecipientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'organs_to_donate','phone_number', 'address']
