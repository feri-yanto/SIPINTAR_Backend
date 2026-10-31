from django.urls import path
from .views import ListedAccount, create_new_account

app_name = 'account'
urlpatterns = [
  path('list-accounts', view=ListedAccount.as_view(), name='list'),
  path('new_account', view=create_new_account, name='create'),
]