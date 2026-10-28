from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

# Create your views here.
@require_GET
def registered_account(request):

  return render(request, template_name='account/page.html', context={
    'title': 'Account',
  })

@require_http_methods(request_method_list=['GET', 'POST'])
def create_new_account(request):

  return render(request, template_name='account/create_by_admin.html', context={
    'title': 'Create new account',
  })