from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from .models import ConsultModel
from .forms import ConsultationForm

# Create your views here.
class ConsultSubmissionView(SuccessMessageMixin, CreateView):
  http_method_names = ['get', 'post']
  model = ConsultModel
  form_class = ConsultationForm
  template_name = 'consult/submission.html'
  success_message = _('Pengajuan berhasil dikirim')

  def get_success_url(self):
    return reverse(viewname='consult:success')

@require_GET
def consult_success_page(request):
  return render(request, template_name='consult/success.html', context={
    'title': 'Pengajuan Berhasil'
  })