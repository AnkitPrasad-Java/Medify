from django.shortcuts import render
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def starters(request):
  return render(request, 'starters.html')


def medicines(request):
  return render(request, 'medicines.html')


def precaution(request):
  return render(request, 'precaution.html')

def appointments(request):
  return render(request, 'appointments.html')

def about(request):
  return render(request,"about.htm")

def book_appointment(request):
  if request.method == 'POST':
    form = AppointmentForm(request.POST)
    if form.is_valid():
        form.save()
        # Redirect to a success page
    else:
        print(form.errors)
  else:
    form = AppointmentForm()

  return render(request, "appointments.html", {"form": form})
