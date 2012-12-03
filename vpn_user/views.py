from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from vpn_user.hashers import MyPBKDF2PasswordHasher
from vpn_user.models import Users
from vpn_user.regist_form import RegistrationForm
from vpn_user.shoot_email import registration_email


def index(request):
    return HttpResponse("Hello, this website is not ready yet!")

def register(request):
    """"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Once is_valid() returns True, the successfully validated form
            # data will be in the form.cleaned_data dict.
            hasher = MyPBKDF2PasswordHasher()
            new_user = Users()
            new_user.username = form.cleaned_data['username']
            # PBKDF2PasswordHasher supports only ASCII.
            new_user.password = hasher.encode(form.cleaned_data['password'].encode('ASCII'),
                                              hasher.salt())
            new_user.active = False;
            new_user.email = form.cleaned_data['email']
            new_user.note = ''
            send_mail('hi', 'test test', 'noreply@yifengliu.com', ['laituan1986@gmail.com'], fail_silently=False)
            new_user.save()
            registration_email(form.cleaned_data['email'])
            return HttpResponseRedirect(reverse('vpn_user.views.thanks'))
        else:
            return HttpResponse("Hello, your info is not valid, try again!" + str(form.errors))
    else:
        form = RegistrationForm()
    return render(request, 'vpn_user/registration.html', {
        'form': form,
    })

def thanks(request):
    """"""
    return render(request, 'vpn_user/thanks.html')
