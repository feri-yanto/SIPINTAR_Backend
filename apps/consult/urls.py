from django.urls import path
from .views import consult_submission_view

app_name = 'consult'
urlpatterns = [
  path('submission', view=consult_submission_view, name='submission'),
]
