from django.shortcuts import render

from doctors.models import Doctor
from doctors.models import DoctorSpecialization

# Create your views here.
def home(request):
    doctors = Doctor.objects.all()
    specialization = DoctorSpecialization.objects.all()
    context = {
        'doctor':doctors,
        'specialization':specialization,
    }
    return render(request, 'pages/home.html', context)