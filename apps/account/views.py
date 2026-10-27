from django.shortcuts import render

# Create your views here.
def registered_account(request):

  return render(request, template_name='account/page.html', context={
    'title': 'Account',
  })