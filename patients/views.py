from django.shortcuts import get_object_or_404, render, redirect
from .models import Patient
from .forms import PatientForm
# Create your views here.
def patients_profile(request):
    current_user = request.user
    current_patient = Patient.objects.get(user=current_user)

    if request.method == 'POST' and current_user.is_authenticated:
        form = PatientForm(request.POST, request.FILES)
    
        if form.is_valid():

            current_patient.profile_image = form.cleaned_data['profile_image']
            # current_patient.date_of_birth = form.cleaned_data['dateOfBirth']
            current_patient.date_of_birth = request.POST['dateOfBirth']
            current_patient.blood_group = request.POST['blood_group']
            current_patient.gender = request.POST['gender']
            current_patient.city = form.cleaned_data['city']
            current_patient.state = form.cleaned_data['state']
            current_patient.country = form.cleaned_data['country']

            
            current_patient.save()
        # messages.success(request, 'Profile Successfully Updated')
            return redirect('patients_profile')
    else:
        form = PatientForm()

    context = {
        'patient':current_patient,
        'form':form,
    }
    return render(request, 'patients/patients-profile.html', context)