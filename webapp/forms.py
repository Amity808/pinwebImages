from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# form.Modelforms
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    # We have defined a clean_password2() method to compare the second password against 
    # the first one and raise a validation error if the passwords don’t match.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password don\'t match')
        return cd['password2']

    # e have added validation for the email field that prevents users from registering with an existing
    # email address.
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email is already in use')
        return data


# for profile settings

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    """
    validation for the email field that prevents users from changing their 
    existing email address to an existing email address of another
    """
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data




class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['data_of_birth', 'photo']
