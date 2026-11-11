from django.urls import path
from .views import ListedAccount, create_new_account, UpdateProfileAccount, DeleteAccount

app_name = 'account'
urlpatterns = [
  path('list-accounts', view=ListedAccount.as_view(extra_context={'title': 'Akun Terdaftar'}), name='list'),
  path('new-account', view=create_new_account, name='create'),
  path('edit-profile/<int:pk>', view=UpdateProfileAccount.as_view(extra_context={'title': 'Edit Profile'}), name='edit'),
  path('delete/<int:pk>', view=DeleteAccount.as_view(), name='delete')
]