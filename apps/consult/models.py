from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

DIVISION_CHOICES = (
  (None, '-- Pilih Bidang --'),
  ('Bid_1', 'Bidang Pengadaan Pemberhentian dan Informasi'),
  ('Bid_2', 'Bidang Pengembangan, Mutasi dan Promosi'),
  ('Bid_3', 'Bidang Penilaian Kinerja, Disiplin ASN dan Penghargaan'),
)

# Create your models here.
class ConsultModel(models.Model):
  full_name = models.CharField(verbose_name=_('full name'), max_length=50)
  nip = models.CharField(verbose_name=_('nip'), max_length=18, validators=[
    RegexValidator(regex=r"^\d+$", message=_('NIP harus berupa angka'))
  ])
  institution = models.CharField(verbose_name=_('institution'), max_length=50)
  phone_number = models.CharField(verbose_name=_('phone number'), max_length=15, validators=[
    RegexValidator(regex=r"^\d+$", message=_('Nomor HP harus berupa angka'))
  ])
  division = models.CharField(verbose_name=_('division'), max_length=40, choices=DIVISION_CHOICES)
  topic = models.CharField(verbose_name=_('topic'), max_length=100)
  reason = models.TextField(verbose_name=_('reason'), max_length=500, null=True, blank=True)
  created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)

  class Meta:
    db_table = 'consultation'