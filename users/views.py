from django.shortcuts import get_object_or_404, redirect, render

from documents.models import Appointment,MedicalHistory
from .forms import RegistrationForm
from .models import Account
from doctors.models import Doctor,DoctorSpecialization
from patients.models import Patient
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.user_type = user_type
            user.phone_number = phone_number
            user.save()

            messages.success(request, 'You are now registered and can log in')
            return redirect('login')
                    
    else:
        form = RegistrationForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password = password)
        
        if user is not None:
            auth.login(request, user)
            current_user = Account.objects.get(id=request.user.id)
            

            if user.user_type == 'doctor': 
                # print("current user: ", current_user)
                doctor_exists = Doctor.objects.filter(user=current_user)
                if doctor_exists:
                    return redirect('doctor_dashboard')
                else:
                    doctor = Doctor(user=current_user)
                    doctor.save()
                    return redirect('doctor_dashboard')   

            else:
                patient_exists = Patient.objects.filter(user=current_user)
                if patient_exists:
                    return redirect('patient_dashboard')
                else:
                    patient = Patient(user=current_user)
                    patient.save()
                    return redirect('patient_dashboard')
                
            # messages.success(request, 'You are now logged in.')
            #return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials')
            return redirect('login')

    
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')


def doctor_dashboard(request):
    current_user = request.user
    current_doctor = get_object_or_404(Doctor, user=current_user)
    # print(specialization)
    specialization = DoctorSpecialization.objects.filter(doctor=current_doctor)

    appointment = Appointment.objects.filter(appointment__doctor=current_doctor)
    print("Appoi: ",appointment)

    patient_appointment = MedicalHistory.objects.filter(doctor=current_doctor)
    
    # try:
    #     current_doctor = Doctor.objects.get(user=current_user)
    # except Doctor.DoesNotExist:
    #     current_doctor = Doctor(user=current_user)
    #     current_doctor.save()
    # try:
    #     current_doctor = Doctor.objects.get(user=current_user)
    #     specialization = get_object_or_404(DoctorSpecialization, doctor=current_doctor)
    # except:
    #     specialized_doctor = DoctorSpecialization(doctor=current_doctor,specialized_category="Update Profile")
    #     specialized_doctor.save()
    #     specialization = get_object_or_404(DoctorSpecialization, doctor=current_doctor)
            
    context = {
        'doctor': current_doctor,
        'specialization':specialization,
        'appointment': appointment,
        'patient_appointment':patient_appointment,
    }

    return render(request,'users/doctor_dashboard.html', context)

def patient_dashboard(request):
    current_user = request.user
    current_patient = get_object_or_404(Patient, user=current_user)

    current_appointment = MedicalHistory.objects.filter(patient=current_patient) 

    # for medical records check if submitted
  


    context = {
        'patient': current_patient,
        'current_appointment':current_appointment,

    }
    return render(request,'users/patient_dashboard.html', context)