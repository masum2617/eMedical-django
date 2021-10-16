from django import forms
from .models import MedicalHistory
class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        # fields = "__all__"
        fields = ['reason','weight','age', 'previous_operation', 'current_medication', 'other_illness','other_information']

    def __init__(self, *args, **kwargs):
        super(MedicalHistoryForm, self).__init__(*args, **kwargs)
        # self.fields['reason'].widget.attrs['class'] = 'form-control'
        # self.fields['city'].widget.attrs['class'] = 'form-control'
        # self.fields['gender'].widget.attrs['class'] = 'form-control select'
        # self.fields['description'].widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'