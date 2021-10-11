from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Doctor, DoctorSpecialization, Experience, Qualification
from .choices import category
from .forms import DoctorForm
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

            profile_pic = form.cleaned_data['profile_image']
            gender = form.cleaned_data['gender']
            description = form.cleaned_data['description']
            city = form.cleaned_data['city']

            doctor = Doctor(city=city, profile_image=profile_pic, gender=gender, description=description, user=current_user)
            doctor.save()
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
 
