from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'contact_name',
            'contact_body',
            'contact_email',
        ]
