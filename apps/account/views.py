from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods
from django.views.generic.list import ListView
from django.urls import reverse
from django.db import transaction
from django.contrib import messages
from .models import AccountModel
from .forms import RegisterAccountForms, ProfileAccountForm

# Create your views here.
class ListedAccount(ListView):
  http_method_names = ['get']
  model = AccountModel
  template_name = 'account/page.html'
  paginate_by = 4

  def get_queryset(self):
    query = super().get_queryset()

    return query.select_related('profile').exclude(role=1)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({'title': 'Daftar akun'})

    return context

@require_http_methods(request_method_list=['GET', 'POST'])
def create_new_account(request):
  if request.method == 'POST':
    account_form = RegisterAccountForms(data=request.POST)
    profile_form = ProfileAccountForm(data=request.POST)

    if account_form.is_valid() and profile_form.is_valid():
      try:
        with transaction.atomic():
          account = account_form.save()
          profile = profile_form.save(commit=False)

          profile.account = account
          profile_form.save()

        messages.success(request, message='Akun berhasil disimpan')
        return redirect(to=reverse(viewname='account:list'))
      except Exception:
        messages.error(request, message='Terjadi kesalahan saat menyimpan data, mohon coba lagi')

  if request.method == 'GET':
    account_form = RegisterAccountForms()
    profile_form = ProfileAccountForm()

  return render(request, template_name='account/create_by_admin.html', context={
    'title': 'Create new account',
    'account_form': account_form,
    'profile_form': profile_form,
  })