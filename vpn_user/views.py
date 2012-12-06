import datetime
from time import mktime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from vpn_user.hashers import MyPBKDF2PasswordHasher
from vpn_user.models import Users
from vpn_user.models import Log
from vpn_user.regist_form import RegistrationForm
from vpn_user.shoot_email import registration_email
from vpn_user.shoot_email import enable_email
from vpn_user.shoot_email import disable_email
from vpn_user.utils import date_range

BYTES_TO_MEGABYTES = 1024 * 1024

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
            new_user.save()
            registration_email(form.cleaned_data['email'])
            return HttpResponseRedirect(reverse('vpn_user.views.thanks'))
        else:
            return HttpResponse("Hello, your info is not valid, try again!" + str(form.errors))
    else:
        form = RegistrationForm()
        print form.as_table()
        return render(request,
                      'vpn_user/registration.html',
                      {'form': form}
                      )


def thanks(request):
    """"""
    return render(request, 'vpn_user/thanks.html')


@login_required
def user_info(request):
    """This view requires login."""
    return render(request, 
                  'vpn_user/user_info.html',
                  {'obj': Users.objects.all()}
                 )


def enable_disable(request):
    """Enable or disable user service and send notification email."""
    user =  Users.objects.filter(id=request.GET.get('id', ''))[0]
    if user.enabled == False:
        user.enabled = True
        enable_email(user.email, user.username)
    else:
        user.enabled = False
        disable_email(user.email, user.username)
    user.save()
    return HttpResponse()


@login_required
def user_log(request):
    """This view requires login."""
    user =  Users.objects.filter(id=request.GET.get('id', ''))[0]
    log = Log.objects.filter(user=user)
    data = {}
    for obj in log:
        # Client must have disconnected already and have end_time stamp so the
        # date logged is valid.
        if obj.disconnected and obj.end_time != None:
            start = mktime(obj.start_time.timetuple()) + 1e-6*obj.end_time.microsecond
            end = mktime(obj.end_time.timetuple()) + 1e-6*obj.end_time.microsecond
            data[int(start)] = [int(end - start),
                                int(obj.bytes_received),
                                int(obj.bytes_sent)]
    return render(request,
                  'vpn_user/user_log.html',
                  {'log': log, 
                   'data': data}
                )


def base(request):
    """"""
    return render(request,
                  'vpn_user/base.html',
                )
