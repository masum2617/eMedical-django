from django.shortcuts import redirect, render
from .models import DoctorSpecialization
from .choices import category
# Create your views here.
def doctor_profile(request):

    specialization = DoctorSpecialization.objects.all()
    # print(specialization)
    context = {
        'specialization': specialization,
        'category':category,
    }
    return render(request, 'doctors/doctor-profile.html', context)

def doctor_specialization(request):
    if request.method == 'POST':
        category = request.POST.getlist('category')
        print(category)
        for i in range(len(category)):
            print(category[i])
            specialized_category = DoctorSpecialization(specialized_category=category[i])
            specialized_category.save()
        return redirect('doctor_profile')


 
