from django.shortcuts import get_object_or_404, render, redirect
from .models import Patient
from doctors.models import Doctor
from documents.models import Prescription
from .forms import PatientForm

# for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

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

def getPrescription(request):
    current_user = request.user
    try:
        current_patient = get_object_or_404(Patient, user=current_user)
    except:
        raise ValueError('no patient found')
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    pres = Prescription.objects.filter(patient=current_patient)

    lines = []

    for pres in pres:
        lines.append("********* MediHelp *************")
        lines.append(" ")
        lines.append("========== Patient Medical History ===============")
        lines.append("First Name: "+pres.name)
        lines.append("Last Name: "+pres.quantity)
        lines.append("Reason For Visit: "+pres.days)
        lines.append("Height: "+pres.morning)
        # lines.append("Age: "+pres.)
        # lines.append("Gender: "+str(hist.gender))
        # lines.append("Blood Group: "+hist.blood_group)
        # lines.append("Previous Operation: "+hist.previous_operation)
        # lines.append("Current Medicaion: "+hist.current_medication)
        # lines.append("Other Illness: "+hist.other_illness)
        # lines.append("Other Information: "+hist.other_information)
        # lines.append("==========================================")
        

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='prescription.pdf')


# def profile_patient(request, patient_id):
#     current_user = request.user
#     # current_patient = get_object_or_404(Patient, user=current_user)
    
#     patient = Patient.objects.get(id=patient_id)
#     # specialization = DoctorSpecialization.objects.get(doctor=doctor)

#     context = {
#         'patient': patient,
#     }
#     return render(request, 'patients/profile_patient.html', context)

