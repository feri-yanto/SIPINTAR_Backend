import os
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible


GOLONGAN_ASN = (
  ('Ia', 'Juru Muda I/a'),
  ('Ib', 'Juru Muda Tingkat I I/b'),
  ('Ic', 'Juru I/c'),
  ('Id', 'Juru Tingkat I I/d'),
  ('IIa', 'Pengatur Muda II/a'),
  ('IIb', 'Pengatur Muda Tingkat I II/b'),
  ('IIc', 'Pengatur II/c'),
  ('IId', 'Pengatur Tingkat I II/d'),
  ('IIIa', 'Penata Muda III/a'),
  ('IIIb', 'Penata Muda Tingkat I III/b'),
  ('IIIc', 'Penata III/c'),
  ('IIId', 'Penata Tingkat I III/d'),
  ('IVa', 'Pembina IV/a'),
  ('IVb', 'Pembina Tingkat I IV/b'),
  ('IVc', 'Pembina Utama Muda IV/c'),
  ('IVd', 'Pembina Utama Madya IV/d'),
  ('IVe', 'Pembina Utama IV/e'),

  ('I', 'Golongan I (PPPK)'),
  ('II', 'Golongan II (PPPK)'),
  ('III', 'Golongan III (PPPK)'),
  ('IV', 'Golongan IV (PPPK)'),
  ('V', 'Golongan V (PPPK)'),
  ('VI', 'Golongan VI (PPPK)'),
  ('VII', 'Golongan VII (PPPK)'),
  ('VII', 'Golongan VIII (PPPK)'),
  ('IX', 'Golongan IX (PPPK)'),
  ('X', 'Golongan X (PPPK)'),
  ('XI', 'Golongan XI (PPPK)'),
  ('XII', 'Golongan XII (PPPK)'),
  ('XIII', 'Golongan XIII (PPPK)'),
  ('XIV', 'Golongan XIV (PPPK)'),
  ('XV', 'Golongan XV (PPPK)'),
  ('XVI', 'Golongan XVI (PPPK)'),
  ('XVII', 'Golongan XVII (PPPK)'),
)

GENDER = (
  ('L', 'Laki-Laki'),
  ('P', 'Perempuan'),
)

# Create your models here.
class AccountModel(AbstractUser):
  # modify existing field
  username = models.CharField(verbose_name=_('username'), max_length=18, unique=True, db_column='nip')
  email = models.EmailField(verbose_name=_('email address'), unique=True, null=True, blank=True)
  first_name = None
  last_name = None

  class RoleChoices(models.IntegerChoices):
    ADMIN = 1, _('admin')
    VERIFICATOR = 2, _('Kabid/Kasubbag')
    USER = 3, _('staff')

  role = models.IntegerField(verbose_name=_('role'), choices=RoleChoices.choices, default=RoleChoices.USER)

  class Meta:
    db_table = 'account'


@deconstructible
class UploadToPath:
  def __init__(self, base_folder):
    self.base_path = base_folder

  def __call__(self, instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{instance.full_name}_{datetime.date.today()}.{ext}'

    return os.path.join(self.base_path, new_filename)

class ProfileAccountModel(models.Model):
  account = models.OneToOneField(to='account.AccountModel', on_delete=models.CASCADE, verbose_name=_('account'), related_name='profile')
  full_name = models.CharField(verbose_name=_('first name'), max_length=150)
  first_title = models.CharField(verbose_name=_('first title'), max_length=20, null=True, blank=True)
  last_title = models.CharField(verbose_name=_('last title'), max_length=20, null=True, blank=True)
  level = models.CharField(verbose_name=_('level'), max_length=20, choices=GOLONGAN_ASN, default='IIIa')
  position = models.CharField(verbose_name=_('position'), max_length=100)
  birthday = models.DateField(verbose_name=_('date birthday'))
  gender = models.CharField(verbose_name=_('gender'), max_length=10, choices=GENDER, default='L')
  picture = models.ImageField(verbose_name=_('picture profile'), null=True, blank=True, upload_to=UploadToPath('images/user/profile/'), validators=[
    FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg'], message=_('Format gambar tidak sesuai, pastikan berformat .jpg, .png, .svg'))
  ])
  signature = models.ImageField(verbose_name=_('signature'), upload_to=UploadToPath('images/user/signature/'), validators=[
    FileExtensionValidator(allowed_extensions=['png'], message=_('Format gambar tidak sesuai, pastikan berformat .png'))
  ])


  class Meta:
    db_table = 'account_profile'