from django.shortcuts import get_object_or_404, redirect, render


from .forms import MedicalHistoryForm
from .models import Appointment, MedicalHistory
from patients.models import Patient
from doctors.models import Doctor,DoctorSpecialization

# Create your views here.
def history(request):
    #doctor = Doctor.objects.get(id=doctor_id)
    #doctor_id = Doctor.objects.get(id=doctor_id)
    current_user = request.user
    current_patient = get_object_or_404(Patient, user=current_user)
    patient = MedicalHistory.objects.filter(patient=current_patient)

    first_name = current_patient.user.first_name
    last_name = current_patient.user.last_name
    gender = current_patient.gender
    #doctor = Doctor.objects.get(id=doctor_id)
    # medical_historyForm = MedicalHistory.objects.all()

    if request.method == 'POST':
        try:
            medical_history = MedicalHistory.objects.get(patient=current_patient, is_processing=False)
        except:
            raise ValueError('Cannot Edit')
        
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():

            medical_history.first_name = first_name
            medical_history.last_name = last_name
            medical_history.gender = gender
            medical_history.reason = form.cleaned_data['reason']
            # height = form.cleaned_data['height']
            medical_history.blood_group = request.POST['blood_group']
            medical_history.weight = form.cleaned_data['weight']
            medical_history.age = form.cleaned_data['age']
            medical_history.previous_operation = form.cleaned_data['previous_operation']
            medical_history.current_medication = form.cleaned_data['current_medication']
            medical_history.other_illness = form.cleaned_data['other_illness']
            medical_history.other_information = form.cleaned_data['other_information']
            medical_history.is_processing = True
            medical_history.save()


            # sending this medical history form as an appointment to the appointment table
            
            appointment = Appointment(appointment=medical_history)
            appointment.save()



            # age = form.cleaned_data['age']
            # gender = form.cleaned_data['gender']
            
            # previous_operation = form.cleaned_data['previous_operation']
            # current_medication = form.cleaned_data['current_medication']
            # other_illness = form.cleaned_data['other_illness']
            # other_information = form.cleaned_data['other_information']

            # medicalHistory = MedicalHistory(reason=reason, weight=weight, age=age,gender=gender, previous_operation=previous_operation, current_medication=current_medication, other_illness=other_illness, other_information=other_information, patient=patient)
            # medicalHistory = MedicalHistory(reason=reason, weight=weight, patient=current_patient)
            # medicalHistory.save()
            return redirect('home')
    else:
        form = MedicalHistoryForm()

    context = {
        'form':form,
    }
    return render(request, 'documents/medical_history.html', context)

def add_prescription(request, patient_id):
    current_user = request.user
    current_doctor = get_object_or_404(Doctor,user=current_user)
    patient = Patient.objects.get(id=patient_id)
    # print("IDDDDD: ",patient)
    doctor_for_patient = MedicalHistory.objects.get(patient=patient,doctor=current_doctor)
    print(doctor_for_patient)

    speciality = DoctorSpecialization.objects.get(doctor=current_doctor)

    context = {
        'current_patient':patient,
        'doctor_for_patient': doctor_for_patient,
        'current_doctor' : current_doctor,
        'speciality':speciality,
        # 'form':form,
    }

    return render(request, 'documents/add_prescription.html', context)