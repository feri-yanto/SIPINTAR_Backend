from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({
      'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20',
      'placeholder': 'Masukan NIP anda'
    })
    self.fields['password'].widget.attrs.update({
      'class': 'h-10 px-3 py-2 rounded-lg text-sm bg-transparent border border-border outline-0 focus-visible:border-blue-500 focus-visible:ring-2 focus-visible:ring-blue-500/20',
      'placeholder': '\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022'
    })

    self.error_messages = {
      "invalid_login": _(
        "Akun tidak ditemukan, pastikan NIP dan sandi sudah benar!"
      ),
      "inactive": _("Akun ini tidak aktif."),
    }