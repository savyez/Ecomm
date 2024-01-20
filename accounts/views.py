from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)

def login(request):
    return HttpResponse('Login')
