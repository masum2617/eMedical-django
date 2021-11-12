import datetime
from re import split
from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render

from documents.models import MedicalHistory
from patients.models import Patient
from .models import Doctor, DoctorSpecialization, Experience, Qualification,AppointmentTime,PatientAppointment
from .choices import category, fromTimeChoice,toTimeChoice
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
    try:
        booked_doctor = MedicalHistory.objects.get(doctor=doctor, patient=current_patient)
    except:
        booked_doctor = MedicalHistory(doctor=doctor, patient=current_patient)
        booked_doctor.save()

    appoint_time_doctor = AppointmentTime.objects.filter(doctor=doctor)
    # day_doc_appoint = AppointmentTime.objects.get(doctor=doctor)
    # print("AAAA: ", appoint_time_doctor)
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

    appoint_day = appoint_time_doctor.values_list('day',flat=True).distinct()
    appoint_date = appoint_time_doctor.values_list('appointment_date', flat=True)
    time_from = appoint_time_doctor.values_list('time_from',flat=True)
    time_to = appoint_time_doctor.values_list('time_to',flat=True)
    print("from: ", time_from)
    context = {
        'doctor':doctor,
        # 'form':form,
        'appoint_time_doctor' : appoint_time_doctor,
        # 'day_doc_appoint':day_doc_appoint,
        'appoint_day':appoint_day,
        'time_from': time_from,
        'time_to' : time_to,
        'appoint_date':appoint_date,

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
    doctors = Doctor.objects.order_by('-date_joined') #A hyphen "-" in front of "check_in" indicates descending order. 

    if 'gender_type' in request.GET:
        gender_type = request.GET['gender_type']
        if gender_type:
            doctors = doctors.filter(gender__iexact=gender_type)
            # print("filtered: ",doctors)

    context = {
        'doctors':doctors,
    }
    return render(request, 'doctors/doctor_search.html', context)

def schedule_timing(request, doctor_id):
    current_user = request.user
    doctor = Doctor.objects.get(id=doctor_id)

    # try:
    #     appoint_time = AppointmentTime.objects.get(doctor=doctor)
    # except AppointmentTime.DoesNotExist:
    #     appoint_time = AppointmentTime.objects.create(doctor=doctor)
    #     appoint_time.save()
        # appoint_time = AppointmentTime(doctor=doctor)
    if request.method == "POST":
        # appoint_time = AppointmentTime.objects.get(doctor=doctor)
        # day = request.POST['day']
        time_from = request.POST['time_from']
        time_to = request.POST['time_to']
        appointment_date = request.POST['appointment_date']
        # print("App date: ", appointment_date)
        # print("TYPE: ", type(appointment_date))
        from_to = time_from+"-"+time_to
       
        appointment_date_obj = datetime.datetime.strptime(appointment_date, '%Y-%m-%d')
        day = appointment_date_obj.date().strftime("%A")

        date = appointment_date_obj.date().strftime("%d")
        month = appointment_date_obj.date().strftime("%B")
        print("Date here: ", date)
        print("Month here: ", month)
        print("DDDAAY: ",day)

        appoint_time = AppointmentTime.objects.create(day=day, time_from=time_from, time_to=time_to ,from_to=from_to, appointment_date=appointment_date, doctor=doctor)
        appoint_time.save()
        return redirect(request.path_info)

    context = {
        'doctor':doctor,
        'fromTimeChoice': fromTimeChoice,
        'toTimeChoice' : toTimeChoice,
    }

    return render(request, 'doctors/schedule-timing.html',context)



def patient_appointment(request, doctor_id):
    current_user = request.user
    current_patient = get_object_or_404(Patient, user=current_user)
    
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == "POST":
        
        from_to = str(request.POST['from_to'])
        print("from_to day:", from_to)
        
        splitted_from_to = from_to.split(',')
        print("Split: ", splitted_from_to[1])

        # print("date_split: ", splitted_from_to[2])
        # date = datetime.datetime.strptime(splitted_from_to[2], '%Y-%m-%d')
        # date_obj = date.date()
        # print("DATEWWW: ", date)
        doc_appoint = PatientAppointment(appoint_day=splitted_from_to[1], appoint_time=splitted_from_to[0], doctor=doctor, patient=current_patient)
        doc_appoint.save()



        return redirect('history') 
