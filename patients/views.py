from django.shortcuts import render


def home(request):
    return render(request, 'patients/home.html')

def add_patient(request):
    return render(request, 'patients/add_patient.html')

def view_patient(request):
    return render(request, 'patients/view_patient.html')

def dashboard(request):
    return render(request, 'patients/dashboard.html')

