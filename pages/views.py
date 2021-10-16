from django.shortcuts import render

from doctors.models import Doctor

# Create your views here.
def home(request):
    doctors = Doctor.objects.all()
    context = {
        'doctor':doctors,
    }
    return render(request, 'pages/home.html', context)