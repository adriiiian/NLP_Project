from django.forms import ModelForm
from sent_analysis.models import SentAnalysis
from django import forms

class SentAnalysisForm(ModelForm):
    class Meta:
        model = SentAnalysis
        fields = ('sentence',)

        labels = {
            'sentence': 'Enter sentence: ',
        }

        widgets = {
            'sentence': forms.TextInput(attrs={'class': 'form-control'})
        }