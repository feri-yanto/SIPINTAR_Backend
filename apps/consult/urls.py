from django.urls import path
from .views import ConsultSubmissionView, consult_success_page

app_name = 'consult'
urlpatterns = [
  path('submission', view=ConsultSubmissionView.as_view(extra_context={'title': 'Pengajuan Konsultasi'}), name='submission'),
  path('success', view=consult_success_page, name='success')
]
