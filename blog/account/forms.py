from account.models import User
from account.tasks import send_email_with_activation_link
from django import forms
from django.db import transaction


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean(self):
        clean_data: dict = super().clean()
        if clean_data['password1'] != clean_data['password2']:
            self.add_error('password1', 'Password mismatch.')
            # raise forms.ValidationError
        # if not clean_data['username']:
        #     pass

        return clean_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Email already exists.')
        return email

    # def save(self, commit=True):
    #     instance: User = super().save(commit=False)
    #     instance.is_active = False
    #
    #     instance.save()
    #
    #     send_email_with_activation_link.apply_async(args=[instance.id], countdown=10)
    #
    #     return instance

    @transaction.atomic
    def save(self, commit=True):
        instance: User = super().save(commit=False)
        instance.is_active = False
        instance.set_password(self.cleaned_data["password1"])
        instance.save()
        send_email_with_activation_link.apply_async(args=[instance.id])
        return instance
