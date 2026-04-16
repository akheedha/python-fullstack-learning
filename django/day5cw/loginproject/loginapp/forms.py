from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']

        if "@gmail.com" in email:
            raise forms.ValidationError("Gmail addresses are not allowed.")

        return email

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters.")

        return password