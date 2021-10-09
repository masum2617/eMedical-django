from django.shortcuts import render

# Create your views here.
def patients_profile(request):
    return render(request, 'patients/patients-profile.html')