from django import forms
from src.models import Branch


class BankForm(forms.ModelForm):
    ifsc = forms.CharField(label="IFSC Code", max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter IFSC code'
    }))

    city = forms.CharField(label="City Name", max_length=500, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control ',
        'placeholder': 'Enter city name'
    }))

    class Meta:
        model = Branch
        fields = ['ifsc', 'bank', 'city']
