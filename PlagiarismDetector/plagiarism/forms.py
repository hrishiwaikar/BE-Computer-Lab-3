from django import forms

class MyForm(forms.Form):
    textbox1=forms.CharField(label='First Text File',widget=forms.Textarea(attrs={'cols': 40, 'rows': 15}),required=False)
    textbox2 =forms.CharField(label='Second Text File',widget=forms.Textarea(attrs={'cols': 40, 'rows':
        15}),required=False)
    textbox3 = forms.CharField(label='Third Text File', widget=forms.Textarea(attrs={'cols': 40, 'rows': 15}),
                               required=False)

class TestForm(forms.Form):
    testText = forms.CharField(label='Test Text ', widget=forms.Textarea(attrs={'cols':40, 'rows':10}),required = False)
