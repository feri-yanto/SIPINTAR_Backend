from django.urls import path
from .views import ListedAccount, create_new_account, UpdateProfileView

app_name = 'account'
urlpatterns = [
  path('list-accounts', view=ListedAccount.as_view(extra_context={'title': 'Akun Terdaftar'}), name='list'),
  path('new-account', view=create_new_account, name='create'),
  path('edit-profile/<int:pk>', view=UpdateProfileView.as_view(extra_context={'title': 'Edit Profile'}), name='edit'),
]