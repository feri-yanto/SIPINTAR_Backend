from django.urls import path
from .views import registered_account

app_name = 'account'
urlpatterns = [
  path('mine', view=registered_account, name='main'),
]