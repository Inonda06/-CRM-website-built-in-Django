from django import forms
from .models import Lead,Agent

class LeadModelForm(forms.ModelForm):
    class Meta:
        model= Lead
        fields=(
            'first_name',
            'Last_name',
            'age',
            'agent',
        )

class LeadForm(forms.Form):
    first_name=forms.CharField()
    Last_name=forms.CharField()
    age= forms.IntegerField(min_value=0)