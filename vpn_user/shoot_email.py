from django.core.mail import send_mail


def registration_email(recipient):
    subject = 'Welcome to jimovpn'
    msg = """Welcome to jimovpn

You will receive another notification email as soon as the admin activates your account.

If you have any questions abou the system, feel free to contact us anytime at admin@yifengliu.com.

The jimovpn team,
An Automatic joint."""
    send_mail(subject, msg, '', [recipient], fail_silently=False)
