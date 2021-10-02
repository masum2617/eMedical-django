from django import forms
from .models import MedicalHistory
class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        models = MedicalHistory
        fields = ['reason', 'ever_had', 'height' 'weight', 'age', 'gender', 'previous_operation', 'current_medication', 'other_illness', 'other_information']