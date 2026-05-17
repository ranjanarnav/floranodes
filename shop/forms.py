from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'discord', 'message']  # Added discord
        widgets = {
            'name': forms.TextInput(attrs={'class': 'rounded-lg px-4 py-2 bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-primary'}),
            'email': forms.EmailInput(attrs={'class': 'rounded-lg px-4 py-2 bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-primary'}),
            'discord': forms.TextInput(attrs={'class': 'rounded-lg px-4 py-2 bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Discord#1234'}),
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'rounded-lg px-4 py-2 bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-primary'}),
        }
