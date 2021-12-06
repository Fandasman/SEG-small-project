from django import forms
from django.core.validators import RegexValidator
from .models import User, ClubMember
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
    password_confirmation = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

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

class ClubApplicationForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = []
        statement = forms.CharField(
            label = "Why would you like to be a member of this club?",
            widget = forms.Textarea()
        )

    def save(self):
        super().save(commit=False)
        club_member = ClubMember.objects.create_club_member(
                user = self.cleaned_data.get('user'),
                club = self.cleaned_data.get('club')
            )
        return club_member

