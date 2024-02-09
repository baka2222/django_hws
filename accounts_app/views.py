from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models, forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm


class SignUpView(generic.CreateView):
    model = models.AccountModel
    form_class = forms.AccountForm
    template_name = 'verify/register.html'
    context_object_name = 'form'
    success_url = '/signin/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        else:
            return redirect('/')

    def get_success_url(self):
        return self.success_url


class SignInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'verify/login.html'

    def get_success_url(self):
        return reverse('accounts_list')


class SignOutView(LogoutView):
    # template_name = 'verify/logout.html'
    next_page = '/'


class AccuntListView(generic.ListView):
    template_name = 'verify/list.html'
    model = models.AccountModel
    context_object_name = 'acc'

    def get_queryset(self):
        return models.AccountModel.objects.all()