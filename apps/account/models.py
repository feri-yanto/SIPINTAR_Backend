from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AccountModel(AbstractUser):
  email = models.EmailField(verbose_name=_('email address'), unique=True, null=True, blank=True)
  first_name = None
  last_name = None

  nip = models.CharField(verbose_name=_('nip'), max_length=18, unique=True)

  REQUIRED_FIELDS = ['email', 'nip'] 

  class Meta:
    db_table = 'account'