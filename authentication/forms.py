from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    display_name = forms.CharField(max_length=30)
    password = forms.CharField()