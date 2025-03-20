from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Iska'})
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'ejemplo@mail.com'})
    )
    message = forms.CharField(
        required=True,
        label="Mensaje",
        widget=forms.Textarea(attrs={'class': 'textarea-field', 'placeholder': 'Escribe tu mensaje aquí...', 'rows': 4})
    )
