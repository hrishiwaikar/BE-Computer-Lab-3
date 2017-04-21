from django import forms

class NumbersForm(forms.Form):
    inputNumbers = forms.CharField(label='Unsorted Numbers',max_length=100)
