import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import AccountModel, ProfileAccountModel

class RegisterAccountForms(forms.ModelForm):
  password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={
    'placeholder': '\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022',
    'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
  }))

  class Meta:
    model = AccountModel
    fields = ['username', 'email', 'password', 'role']
    error_messages = {
      'username': {
        'unique': _('NIP sudah terdaftar')
      },
      'email': {
        'unique': _('Email sudah terdaftar'),
        'invalid': _('Pastikan format email sudah benar')
      },
    }
    widgets = {
      'username': forms.NumberInput(attrs={
        'autofocus': True,
        'placeholder': '2000xxxxxx',
        'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
      }),
      'email': forms.EmailInput(attrs={
        'placeholder': 'emailanda@contoh.com',
        'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
      }),
      'role': forms.RadioSelect()
    }

  def clean_username(self):
    username_as_nip = self.cleaned_data.get('username')

    if username_as_nip and not username_as_nip.isdigit():
      raise ValidationError(message=_('NIP hanya dapat berupa angka'), code='invalid')

    return username_as_nip

  def clean_password(self):
    password = self.cleaned_data.get('password')
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"

    if password and re.match(pattern, password) is None:
      raise ValidationError(message=[
        'Sandi harus memiliki 8 karakter',
        'Sandi harus memiliki huruf besar dan kecil',
        'Sandi harus memiliki angka'
      ], code='invalid')

    return password

  def save(self, commit: bool = True):
    password = self.cleaned_data.get('password')
    instance = super().save(commit=False)

    instance.set_password(password)

    if commit:
      instance.save()

    return instance


class ProfileAccountForm(forms.ModelForm):
  class Meta:
    model = ProfileAccountModel
    fields = '__all__'
    exclude = ['account']
    widgets = {
      'first_name': forms.TextInput(attrs={
        'placeholder': 'John',
        'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
      }),
      'last_name': forms.TextInput(attrs={
        'placeholder': 'Doe',
        'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
      }),
      'first_title': forms.TextInput(attrs={
        'placeholder': 'dr/ir/prof/...',
        'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
      }),
      'last_title': forms.TextInput(attrs={
        'placeholder': 'SE/S.Pd/S.Kom/S.Sos/...',
        'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
      }),
      'position': forms.TextInput(attrs={
        'placeholder': 'Analis SDM Aparatur Ahli Muda',
        'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20'
      })
    }