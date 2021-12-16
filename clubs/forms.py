from django import forms
from django.core.validators import RegexValidator
from .models import User, Club, Tournament, ClubMemberApplications
from django.contrib.auth.forms import UserChangeForm

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "experience", "bio"]
        widgets = { "bio": forms.Textarea() }

    new_password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        validators=[
            RegexValidator(
                regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
                message = 'The password must contain an uppercase, lowercase and numeric characters!'
                )
        ]
    )
    password_confirmation = forms.CharField(label="Confirm password", widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'The confirmation does not match the original password.')

    def save(self):
        super().save(commit=False)
        user = User.objects.create_user(
                self.cleaned_data.get('username'),
                first_name = self.cleaned_data.get('first_name'),
                last_name = self.cleaned_data.get('last_name'),
                email = self.cleaned_data.get('email'),
                experience = self.cleaned_data.get('experience'),
                bio = self.cleaned_data.get('bio'),
                password = self.cleaned_data.get('new_password'),
            )
        return user

class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "experience", "bio"]
        widgets = { "bio": forms.Textarea() }

class PasswordForm(forms.Form):
    """Form for changing the password."""

    password = forms.CharField(label = 'Current password', widget = forms.PasswordInput())
    new_password = forms.CharField(
        label = 'New password',
        widget = forms.PasswordInput(),
        validators = [RegexValidator(
            regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
        )]
    )
    password_confirmation = forms.CharField(label = 'Confirm password', widget = forms.PasswordInput())

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password_confirmation != new_password:
            self.add_error('password_confirmation', "Passwords don't match!")


class ClubCreationForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ["name", "location", "description"]
        widgets = { "description": forms.Textarea() }

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ["name", "description", "capacity", "deadline", "start"]
        widgets = {"description": forms.Textarea()}

class PassOwnershipForm(forms.Form):

    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label="Confirm password", widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password_confirmation != password:
            self.add_error('password_confirmation', "Passwords don't match!")

class ClubApplicationForm(forms.ModelForm):
    class Meta:
        model = ClubMemberApplications
        fields = ["personal_statement"]
        widgets = { "personal_statement": forms.Textarea() }
