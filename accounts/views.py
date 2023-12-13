from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import ConfiguracionPagina
# Create your views here.


class InicioView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        configuracion = ConfiguracionPagina.objects.first()

        context['title_page'] = configuracion.titulo if configuracion else 'SIGECOR'
        return context







class Dashboard(ListView):
    def get(self, request, *args, **kwargs):
            return render(request, 'dashboard/home.html')


class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        else:
            return render(request, 'auth/signup.html', {"form": UserCreationForm})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            try:
                user = form.save()
                login(request, user)
                messages.success(request, '¡Registro exitoso!')
                return redirect('accounts:home')
            except IntegrityError:
                messages.error(request, 'Nombre de usuario ya tomado.')
        else:
            messages.error(request, 'Ha ocurrido un error en el formulario. Por favor, inténtalo de nuevo.')

        return render(request, 'auth/signup.html', {"form": UserCreationForm})

class SigninView(LoginView):
    def get(self, request):
        if (request.user.is_authenticated):
            return redirect ('accounts:home')
        else:
            return render(request, 'auth/signin.html', {"form": AuthenticationForm()})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:home')
        return render(request, 'auth/signin.html', {"form": form, "error": "Nombre de usuario o contraseña incorrecta."})

class SignoutView(LogoutView):
    next_page = ('accounts:index')