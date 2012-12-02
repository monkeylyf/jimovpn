from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

attrs_dict = {'class': 'required'}

class RegistrationForm(forms.Form):

    """Form for new user to register a new account."""

    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={'invalid': _( \
                                    'This value may contain only letters, '
                                    'numbers and @/./+/-/_ characters.')})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                    maxlength=75)),
                             label=_('E-mail'))
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                          render_value=False),
                               label=_('Password'))
    check_pw = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                          render_value=False),
                               label=_('Password (again)'))

    def clean_username(self):
        """Validate that the username is alphanumeric and it not registered."""
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_('A user with that username already exists.'))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """Verifiy that the values entered into the two password fields match.

        Note that an error here will end up in 'non_field_errors()' because it
        doesn't apply to a single field.
        """
        if 'password' in self.cleaned_data and 'check_pw' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['check_pw']:
                raise forms.ValidationError(_('The two password fields do not match.'))
        return self.cleaned_data
