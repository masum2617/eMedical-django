from django.shortcuts import redirect, render
from .forms import RegistrationForm
from .models import Account
from doctors.models import Doctor
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
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
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
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

    current_doctor = Doctor.objects.get(user=current_user)

    context = {
        'doctor': current_doctor,
    }

    return render(request,'users/doctor_dashboard.html',context)

def patient_dashboard(request):
    return render(request,'users/patient_dashboard.html')