from django.shortcuts import get_object_or_404, redirect, render

from documents.models import MedicalHistory
from documents.models import Prescription

from .forms import RegistrationForm
from .models import Account
from doctors.models import Doctor,DoctorSpecialization,AppointmentTime
from patients.models import Patient,PrescriptionStatus
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
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

    # appointment = Appointment.objects.filter(appointment__doctor=current_doctor)
    # print("Appoi: ",appointment)

    patient_appointment = MedicalHistory.objects.filter(doctor=current_doctor)

    if request.method == 'POST':
        patient_id = request.POST['status']
        accepted_patient = MedicalHistory.objects.get(id=patient_id)
        accepted_patient.is_active = True
        accepted_patient.save()
        return redirect('doctor_dashboard')
        # print("VALUE: ", value)

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
        # 'appointment': appointment,
        'patient_appointment':patient_appointment,
    }

    return render(request,'users/doctor_dashboard.html', context)

def patient_dashboard(request):
    current_user = request.user
    current_patient = get_object_or_404(Patient, user=current_user)

    current_appointment = MedicalHistory.objects.filter(patient=current_patient) 

    prescription = Prescription.objects.filter(patient=current_patient)

    # checking from prescription status for one doctor one prescript

    prescription_status = PrescriptionStatus.objects.filter(patient=current_patient,is_uploaded=True)

    # city= prescription.doctor.city
    # print("PRES: ", city)

    # pres_one_doc = prescription.values_list('doctor', flat=True).distinct()
    # print("one: ", pres_one_doc)
    # current_doctor = get_object_or_404(Doctor, doctor=current_appointment.doctor)
    # for medical records check if submitted
  
    # appointment_for_patient = AppointmentTime.objects.filter(patient=current_patient)

    # print(appointment_date)
    


    context = {
        'patient': current_patient,
        'current_appointment':current_appointment,
        'prescription':prescription,
        'prescription_status':prescription_status,

    }
    return render(request,'users/patient_dashboard.html', context)


def status(request, patient_id):
    
    # current_patient = get_object_or_404(Patient, user=current_user)
    current_user = request.user
    current_doctor = get_object_or_404(Doctor,user=current_user)
    patient = Patient.objects.get(id=patient_id, doctor=current_doctor)


    patientMedicalHistory = MedicalHistory.objects.get(patient=patient)
    patientMedicalHistory.is_active = True
    patientMedicalHistory.save()
    return redirect('doctor_dashboard')

def current_patient(request, patient_id):
    current_user = request.user
    current_doctor = get_object_or_404(Doctor,user=current_user)
    patient = Patient.objects.get(id=patient_id)
    # print("IDDDDD: ",patient)
    doctor_for_patient = MedicalHistory.objects.get(patient=patient,doctor=current_doctor)
    print(doctor_for_patient)

    prescriptions = PrescriptionStatus.objects.filter(doctor=current_doctor)
    presc_patient = Prescription.objects.filter(patient=patient, doctor=current_doctor)
    # presc_patient_single = presc_patient.values_list('patient', flat=True).distinct()
    context = {
        'current_patient':patient,
        'doctor_for_patient': doctor_for_patient,
        'prescriptions': prescriptions,
        'presc_patient':presc_patient,
        # 'presc_patient_single':presc_patient_single,
    }

    return render(request, 'users/current-patient.html', context)

def getPrescriptionForDoc(request, patient_id):
    current_user = request.user
    current_doctor = get_object_or_404(Doctor,user=current_user)
    patient = Patient.objects.get(id=patient_id)

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    pres = Prescription.objects.filter(patient=patient, doctor=current_doctor)

    lines = []
    # lines.append("********* MediHelp *************")
    lines.append(" ")
    lines.append("************MediHelp Prescription************")
    lines.append("Patient Name: "+patient.user.first_name+" "+patient.user.last_name)
    lines.append("Doctor Name: Dr. "+current_doctor.user.first_name+" "+current_doctor.user.last_name)
    # lines.append("Drug Name "+"Quantity "+"Days to Take "+"Time 1 "+"Time 2 "+"Time 3"+"Time 4 ")
    for pres in pres:
        lines.append("==============================")
        lines.append("Drug Name: "+pres.name)
        lines.append("Quantity: "+pres.quantity)
        lines.append("Days: "+pres.days)
        lines.append("Time Slot 1: "+pres.morning)
        lines.append("Time Slot 2: "+pres.afternoon)
        lines.append("Time Slot 3: "+pres.evening)
        lines.append("Time Slot 4: "+pres.night)
   
        lines.append("==============================")
        

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='prescription.pdf')
