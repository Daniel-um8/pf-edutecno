from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    email = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo'})
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tu mensaje'})
    )
