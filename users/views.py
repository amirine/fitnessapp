from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    """View for User registration"""
    form_class = RegisterUserForm
    template_name = 'home/register_page.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Redirection to Home page in case of successful registration"""
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')


class LoginUser(LoginView):
    """View for User login"""
    form_class = LoginUserForm
    template_name = 'home/login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


def logout_user(request):
    """View for User logout"""
    logout(request)
    return redirect('login')

# class TestLoginUser(LoginView):
#     """View for User login"""
#     form_class = LoginUserForm
#     template_name = 'home/login_page.html'
#
#     def get_success_url(self):
#         return reverse_lazy('dashboard')
#
#
# class TestRegisterUser(CreateView):
#     """View for User registration"""
#     form_class = RegisterUserForm
#     template_name = 'home/register_page.html'
#     success_url = reverse_lazy('test_login')
#
#     def form_valid(self, form):
#         """Redirection to Home page in case of successful registration"""
#         user = form.save()
#         login(self.request, user)
#         return redirect('dashboard')