from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

GOLONGAN_ASN = (
  ("Ia", "Juru Muda I/a"),
  ("Ib", "Juru Muda Tingkat I I/b"),
  ("Ic", "Juru I/c"),
  ("Id", "Juru Tingkat I I/d"),
  ("IIa", "Pengatur Muda II/a"),
  ("IIb", "Pengatur Muda Tingkat I II/b"),
  ("IIc", "Pengatur II/c"),
  ("IId", "Pengatur Tingkat I II/d"),
  ("IIIa", "Penata Muda III/a"),
  ("IIIb", "Penata Muda Tingkat I III/b"),
  ("IIIc", "Penata III/c"),
  ("IIId", "Penata Tingkat I III/d"),
  ("IVa", "Pembina IV/a"),
  ("IVb", "Pembina Tingkat I IV/b"),
  ("IVc", "Pembina Utama Muda IV/c"),
  ("IVd", "Pembina Utama Madya IV/d"),
  ("IVe", "Pembina Utama IV/e"),

  ("I", "Golongan I (PPPK)"),
  ("II", "Golongan II (PPPK)"),
  ("III", "Golongan III (PPPK)"),
  ("IV", "Golongan IV (PPPK)"),
  ("V", "Golongan V (PPPK)"),
  ("VI", "Golongan VI (PPPK)"),
  ("VII", "Golongan VII (PPPK)"),
  ("VII", "Golongan VIII (PPPK)"),
  ("IX", "Golongan IX (PPPK)"),
  ("X", "Golongan X (PPPK)"),
  ("XI", "Golongan XI (PPPK)"),
  ("XII", "Golongan XII (PPPK)"),
  ("XIII", "Golongan XIII (PPPK)"),
  ("XIV", "Golongan XIV (PPPK)"),
  ("XV", "Golongan XV (PPPK)"),
  ("XVI", "Golongan XVI (PPPK)"),
  ("XVII", "Golongan XVII (PPPK)"),
)

# Create your models here.
class AccountModel(AbstractUser):
  # modify existing field
  username = models.CharField(verbose_name=_('username'), max_length=18, unique=True, db_column='nip')
  email = models.EmailField(verbose_name=_('email address'), unique=True, null=True, blank=True)
  first_name = None
  last_name = None

  # New field
  class RoleChoices(models.IntegerChoices):
    ADMIN = 1, _('admin')
    VERIFICATOR = 2, _('verifikator')
    USER = 3, _('staff')

  role = models.IntegerField(verbose_name=_('role'), choices=RoleChoices.choices, default=RoleChoices.USER)

  class Meta:
    db_table = 'account'

class ProfileAccountModel(models.Model):
  account = models.OneToOneField(to='account.AccountModel', on_delete=models.CASCADE, verbose_name=_('account'), related_name='profile')
  first_name = models.CharField(verbose_name=_('first name'), max_length=100)
  last_name = models.CharField(verbose_name=_('last name'), max_length=150, null=True, blank=True)
  first_title = models.CharField(verbose_name=_('first title'), max_length=20, null=True, blank=True)
  last_title = models.CharField(verbose_name=_('last title'), max_length=20, null=True, blank=True)
  level = models.CharField(verbose_name=_('level'), max_length=20, choices=GOLONGAN_ASN, default="IIIa")
  position = models.CharField(verbose_name=_('position'), max_length=100)


  class Meta:
    db_table = 'account_profile'