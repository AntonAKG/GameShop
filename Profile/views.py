from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate

from .forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(self.request, email=email, password=password)

        if user:
            user.set_password(password)
            user.save()

        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class LoginClassView(LoginView):
    LoginView.authentication_form = LoginForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Sign in'

        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Profile'

        return context
