from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    # password = forms.CharField(widget=PasswordInput(attrs={
    #     'placeholder': 'Enter Password',
    #     'class': 'form-control',
    # }))
    class Meta:
        model = Patient
        fields = ['profile_image', 'city', 'state' , 'country']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'upload'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        # self.fields['gender'].widget.attrs['class'] = 'form-control select'
        # self.fields['blood_group'].widget.attrs['class'] = 'form-control select'
        # self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        # self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        # self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = 'form-control'