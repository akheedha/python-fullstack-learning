from django import forms

class RegisterForm(forms.Form):
    fullname = forms.CharField(
        min_length=5,
        max_length=50
    )

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=20
    )