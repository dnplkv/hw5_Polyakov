from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View

from .forms import UserRegistrationForm
from .models import User


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ('first_name', 'last_name',)
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'account/user_sign_up.html'
    success_url = reverse_lazy('home_page')


class ActivateUserView(View):
    def get(self, request, confirmation_token):
        user = get_object_or_404(User, confirmation_token=confirmation_token)
        user.is_active = True
        user.save(update_fields=('is_active',))
        return redirect("home_page")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password saved!')
            return redirect('home_page')
        else:
            messages.error(request, 'Error!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/user_change_password.html', {
        'form': form
    })


def logout(request):
    auth_logout(request)
    return redirect("home_page")
