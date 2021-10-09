from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    # password = forms.CharField(widget=PasswordInput(attrs={
    #     'placeholder': 'Enter Password',
    #     'class': 'form-control',
    # }))
    class Meta:
        model = Doctor
        fields = ['city', 'profile_image', 'gender', 'description']

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'upload'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control select'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        # self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        # self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = 'form-control'