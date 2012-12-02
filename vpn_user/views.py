from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from vpn_user.regist_form import RegistrationForm

def index(request):
    return HttpResponse("Hello, wo hao jimo!")

def register(request):
    """"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Once is_valid() returns True, the successfully validated form
            # data will be in the form.cleaned_data dict.
            new_user = User()
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.password = form.cleaned_data['password']
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegistrationForm()
    return render(request, 'vpn_user/registration.html', {
        'form': form,
    })
