from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import AccountModel, ProfileAccountModel
from .forms import RegisterAccountForms, ProfileAccountForm

# Create your views here.
class ListedAccount(ListView):
  http_method_names = ['get']
  model = AccountModel
  template_name = 'account/list_account.html'
  paginate_by = 2

  def get_queryset(self):
    query = super().get_queryset()

    return query.select_related('profile').exclude(role=1)


@require_http_methods(request_method_list=['GET', 'POST'])
def create_new_account(request):
  if request.method == 'POST':
    account_form = RegisterAccountForms(data=request.POST)
    profile_form = ProfileAccountForm(data=request.POST, files=request.FILES)

    if account_form.is_valid() and profile_form.is_valid():
      try:
        with transaction.atomic():
          account = account_form.save()
          profile = profile_form.save(commit=False)

          profile.account = account
          profile_form.save()

        messages.success(request, message=f'Selamat, akun {profile.full_name} berhasil dibuat')
        return redirect(to=reverse(viewname='account:list'))
      except Exception:
        messages.error(request, message='Terjadi kesalahan saat menyimpan data, mohon coba lagi')

  if request.method == 'GET':
    account_form = RegisterAccountForms()
    profile_form = ProfileAccountForm()

  return render(request, template_name='account/create_by_admin.html', context={
    'title': 'Membuat Akun Pegawai',
    'account_form': account_form,
    'profile_form': profile_form,
  })


class UpdateProfileAccount(SuccessMessageMixin, UpdateView):
  http_method_names = ['get', 'post']
  model = ProfileAccountModel
  form_class = ProfileAccountForm
  template_name = 'account/edit_account.html'
  success_message = 'Data berhasil diubah & disimpan'

  def get_success_url(self) -> str:
    return reverse(viewname=('account:list'))


class DeleteAccount(SuccessMessageMixin, DeleteView):
  http_method_names = ['post']
  model = AccountModel
  success_message = 'Akun berhasil dihapus'

  def get_success_url(self) -> str:
    return reverse(viewname=('account:list'))