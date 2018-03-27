from .models import *
from  django import forms

class VacancyForm(forms.ModelForm):
    class Meta:
        model = VacancyFeedBack
        fields = ['vacancy', 'name', 'email', 'file']