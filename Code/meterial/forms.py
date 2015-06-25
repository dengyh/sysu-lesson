from django import forms

class MeterialForm(forms.Form):
    title = forms.CharField(required=True)
    file = forms.FileField(required=True)