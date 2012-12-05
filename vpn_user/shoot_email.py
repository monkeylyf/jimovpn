from django.core.mail import send_mail


def registration_email(recipient):
    """"""
    subject = 'Welcome to jimovpn'
    msg = """Welcome to jimovpn

You will receive another notification email as soon as the admin activates your account.

If you have any questions about the system, feel free to contact us anytime at admin@yifengliu.com.

The jimovpn team,
An Automatic joint."""
    send_mail(subject, msg, '', [recipient], fail_silently=False)

def enable_email(recipient, username):
    """"""
    subject = 'Your jimovpn account was activated'
    msg = """Hey %s,

You recently created a new account on jimovpn and your service has been activated.

To start quickly, follow the link below:

http://jimovpn.yifengliu.com/user/thanks

The jimovpn team,
An Automatic joint."""% (username, )

    send_mail(subject, msg, '', [recipient], fail_silently=False)

def disable_email(recipient, username):
    """"""
    subject = 'Your jimovpn account was deactivated'
    msg = """Hey %s,

Your jimovpn service has been deactivated.

If you have any questions about the system, feel free to contact us anytime at admin@yifengliu.com.

The jimovpn team,
An Automatic joint."""% (username, )

    send_mail(subject, msg, '', [recipient], fail_silently=False)
