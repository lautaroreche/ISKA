from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Nombre", widget=forms.TextInput(attrs={'placeholder': 'Iska'}))
    email = forms.EmailField(max_length=100, required=True, label="Dirección de correo electrónico", widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@mail.com'}))
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí...'}),
        required=True,
        label="Mensaje"
    )