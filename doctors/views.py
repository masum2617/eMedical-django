from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render

from documents.models import MedicalHistory
from patients.models import Patient
from .models import Doctor, DoctorSpecialization, Experience, Qualification
from .choices import category
from .forms import DoctorForm
from documents.forms import MedicalHistoryForm

# for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.
def doctor_profile(request):
    current_user = request.user
    # specialization = DoctorSpecialization.objects.filter(doctor=)

    current_doctor = get_object_or_404(Doctor, user=current_user)
    # print(specialization)
    specialization = DoctorSpecialization.objects.filter(doctor=current_doctor)

    if request.method == 'POST' and current_user.is_authenticated:
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():

            current_doctor.profile_image = form.cleaned_data['profile_image']
            current_doctor.gender = form.cleaned_data['gender']
            current_doctor.description = form.cleaned_data['description']
            current_doctor.city = form.cleaned_data['city']

            # doctor = Doctor(city=city, profile_image=profile_pic, gender=gender, description=description, user=current_user)
            current_doctor.save()
        # messages.success(request, 'Profile Successfully Updated')
            return redirect('doctor_profile')
    else:
        form = DoctorForm()
    context = {
        'specialization': specialization,
        'category':category,
        'form':form,
        'doctor':current_doctor,
    }
    return render(request, 'doctors/doctor-profile.html', context)

def doctor_specialization(request):
    try:
        current_doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        pass
    if request.method == 'POST':
        category = request.POST.getlist('category')
        # services = request.POST['services']
        # print(category)
        for i in range(len(category)):
            # print(category[i])
            specialized_category = DoctorSpecialization( doctor=current_doctor,specialized_category=category[i])
            specialized_category.save()
        # service = DoctorSpecialization(services=services)
        # service.save()
        return redirect('doctor_profile')

def doctors(request):
    doctors = Doctor.objects.all()

    context = {
        'doctors':doctors,
    }
    return render(request, 'doctors/doctors.html', context)


def qualification(request):
    current_user = request.user

    current_doctor = Doctor.objects.get(user=current_user)
    doctor_exists = Qualification.objects.filter(doctor=current_doctor).exists()
    if doctor_exists == True or doctor_exists == False:
        doctor = Qualification.objects.filter(doctor=current_doctor)

        if request.method == 'POST':
            doctor.qualification_degree = request.POST['degree']
            doctor.institute_name = request.POST['institute']
            doctor.years_of_completion = request.POST['years']

            doctor_qualification = Qualification(institution_name=doctor.institute_name, qualification_degree=doctor.qualification_degree, years_of_completion=doctor.years_of_completion, doctor=current_doctor)

            doctor_qualification.save()

        return redirect('doctor_profile')
    

def experience(request):
    current_user = request.user
    try:
        current_doctor = Doctor.objects.get(user=current_user)
    except Doctor.DoesNotExist:
        pass
    if request.method == 'POST':
        hospital_name = request.POST['hospital']
        worked_from = request.POST['worked_from']
        worked_to = request.POST['worked_to']
        designation = request.POST['designation']

        experience = Experience(hospital_name=hospital_name, worked_from=worked_from, worked_to=worked_to, designation=designation, user=current_doctor)

        experience.save()

        return redirect('doctor_profile')
 
def booking(request, doctor_id):
    current_user = request.user
    current_patient = get_object_or_404(Patient, user=current_user)
    
    doctor = Doctor.objects.get(id=doctor_id)


    # for checking purpose
    booked_doctor = MedicalHistory(doctor=doctor, patient=current_patient)
    booked_doctor.save()

    # medical_historyForm = MedicalHistory.objects.all()

    # if request.method == 'POST':
    #     form = MedicalHistoryForm(request.POST)
    #     if form.is_valid():
    #         first_name = current_patient.user.first_name
    #         last_name = current_patient.user.last_name
            
    #         reason = form.cleaned_data['reason']
    #         # height = form.cleaned_data['height']
    #         weight = form.cleaned_data['weight']
    #         age = form.cleaned_data['age']
    #         gender = form.cleaned_data['gender']
            
    #         previous_operation = form.cleaned_data['previous_operation'].replace(',','')
    #         current_medication = form.cleaned_data['current_medication'].replace(',','')
    #         other_illness = form.cleaned_data['other_illness'].replace(',','')
    #         other_information = form.cleaned_data['other_information'].replace(',','')

    #         medicalHistory = MedicalHistory(first_name=first_name, last_name=last_name, reason=reason, weight=weight, age=age,gender=gender, previous_operation=previous_operation, current_medication=current_medication, other_illness=other_illness, other_information=other_information, patient=current_patient, doctor=doctor)

    #         medicalHistory.save()
    #         return redirect('booking')
    # else:
    #     form = MedicalHistoryForm()

    context = {
        'doctor':doctor,
        # 'form':form,
    }
    return render(request, 'doctors/booking.html', context)

def medical_history(request):

    current_user = request.user
    try:
        current_doctor = get_object_or_404(Doctor, user=current_user)
    except:
        raise ValueError('no doctor found')
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    history = MedicalHistory.objects.filter(doctor=current_doctor)

    lines = []

    for hist in history:
        lines.append("********* MediHelp *************")
        lines.append(" ")
        lines.append("========== Patient Medical History ===============")
        lines.append("First Name: "+hist.first_name)
        lines.append("Last Name: "+hist.last_name)
        lines.append("Reason For Visit: "+hist.reason)
        lines.append("Height: "+hist.weight)
        lines.append("Age: "+hist.age)
        lines.append("Gender: "+str(hist.gender))
        lines.append("Blood Group: "+hist.blood_group)
        lines.append("Previous Operation: "+hist.previous_operation)
        lines.append("Current Medicaion: "+hist.current_medication)
        lines.append("Other Illness: "+hist.other_illness)
        lines.append("Other Information: "+hist.other_information)
        lines.append("==========================================")
        

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='medical_history.pdf')


def profile(request, doctor_id):
    current_user = request.user
    # current_patient = get_object_or_404(Patient, user=current_user)
    
    doctor = Doctor.objects.get(id=doctor_id)
    specialization = DoctorSpecialization.objects.get(doctor=doctor)

    context = {
        'doc_profile':doctor,
        'specialization':specialization,
    }
    return render(request, 'doctors/profile.html', context)


def doctor_search(request):
    doctors = Doctor.objects.order_by('-date_joined') #A hyphen "-" in front of "check_in" indicates descending order. Ascending order is implied

    if 'gender_type' in request.GET:
        gender_type = request.GET['gender_type']
        if gender_type:
            doctors = doctors.filter(gender__iexact=gender_type)
            # print("filtered: ",doctors)

    context = {
        'doctors':doctors,
    }
    return render(request, 'doctors/doctor_search.html', context)


