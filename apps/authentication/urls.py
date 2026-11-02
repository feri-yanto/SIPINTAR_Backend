from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm

app_name = 'authentication'
urlpatterns = [
  path('login', view=LoginView.as_view(
    authentication_form=CustomAuthenticationForm,
    redirect_authenticated_user=True,
    template_name = 'auth/login.html',
    extra_context={'title': 'Login'}
  ), name='login'),
  path('logout', view=login_required(LogoutView.as_view()), name='logout'),
]