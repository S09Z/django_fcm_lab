from django import forms

class MessageForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    image = forms.URLField(required=False)