from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ConsultModel

class ConsultationForm(forms.ModelForm):
  class Meta:
    model = ConsultModel
    fields = '__all__'
    exclude = ('created_at',)

    error_messages = {
      'full_name': {
        'max_length': _('Pastikan masukan anda tidak melebihi 50 Karakter')
      },
      'division': {
        'invalid_choice': _('Pilihan bidang tidak sesuai')
      }
    }

    widgets = {
      'full_name': forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': 'Nama Lengkap',
        'class': 'w-full h-10 px-3 py-2 rounded-lg text-sm bg-background border border-border outline-none focus-visible:border-blue-500 focus-visible:ring-3 focus-visible:ring-blue-500/20 aria-[invalid]:bg-red-50 aria-[invalid]:border-red-500 aria-[invalid]:focus-visible:ring-red-500/20'
      }),
      'nip': forms.NumberInput(attrs={
        'placeholder': '2000xxxxxxxxxxxxxx',
        'class': 'w-full h-10 px-3 py-2 rounded-lg text-sm bg-background border border-border outline-none focus-visible:border-blue-500 focus-visible:ring-3 focus-visible:ring-blue-500/20 aria-[invalid]:bg-red-50 aria-[invalid]:border-red-500 aria-[invalid]:focus-visible:ring-red-500/20'
      }),
      'institution': forms.TextInput(attrs={
        'placeholder': 'Cth. Dinas Pendidikan dan Kebudayaan',
        'class': 'w-full h-10 px-3 py-2 rounded-lg text-sm bg-background border border-border outline-none focus-visible:border-blue-500 focus-visible:ring-3 focus-visible:ring-blue-500/20 aria-[invalid]:bg-red-50 aria-[invalid]:border-red-500 aria-[invalid]:focus-visible:ring-red-500/20'
      }),
      'phone_number': forms.NumberInput(attrs={
        'placeholder': '852xxxxxxxxxx',
        'class': 'w-full h-10 py-2 bg-transparent border-none outline-none'
      }),
      'division': forms.Select(attrs={
        'class': 'select w-full h-10 px-3 py-2 rounded-lg text-sm bg-background border border-border outline-0 shadow-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 open:border-blue-500 open:ring-3 open:ring-blue-500/20 aria-[invalid]:bg-red-50 aria-[invalid]:border-red-500 aria-[invalid]:focus-visible:ring-red-500/20'
      }),
      'topic': forms.TextInput(attrs={
        'placeholder': 'Cth. Menanyakan tentang mutasi ASN',
        'class': 'w-full h-10 px-3 py-2 rounded-lg text-sm bg-background border border-border outline-none focus-visible:border-blue-500 focus-visible:ring-3 focus-visible:ring-blue-500/20 aria-[invalid]:bg-red-50 aria-[invalid]:border-red-500 aria-[invalid]:focus-visible:ring-red-500/20'
      }),
      'reason': forms.Textarea(attrs={
        'placeholder': 'Saya ingin berkonsultasi mengenai .....',
        'class': 'w-full h-40 px-3 py-2 rounded-lg text-sm bg-background border border-border outline-none focus-visible:border-blue-500 focus-visible:ring-3 focus-visible:ring-blue-500/20 aria-[invalid]:bg-red-50 aria-[invalid]:border-red-500 aria-[invalid]:focus-visible:ring-red-500/20',
      })
    }