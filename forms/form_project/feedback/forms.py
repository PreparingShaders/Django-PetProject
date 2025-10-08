from django import forms

class FeedbackForms(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))