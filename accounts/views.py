from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm
from .models import Account

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = Account.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
            )
            user.phone_number = phone_number

            user.save()

    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)

def login(request):
    return HttpResponse('Login')
