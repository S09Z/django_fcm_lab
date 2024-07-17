# fcm_app/forms.py
from django import forms
from .models import FCMToken
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")

        return cleaned_data

class FCMTokenForm(forms.ModelForm):
    class Meta:
        model = FCMToken
        fields = ['token']

class FCMMessageForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = forms.CharField(max_length=255)
