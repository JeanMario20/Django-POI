from django import forms

class CheckForm(forms.Form):
    checkNumber1 = forms.IntegerField(label='Introduce tu numero')