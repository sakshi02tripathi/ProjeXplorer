from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import TechStack, Interest, Domain, UserSkill

# Define proficiency levels
PROFICIENCY_LEVELS = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class SkillForm(forms.Form):
    tech_stacks = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Programming Languages / Tech Stacks'
    )
    proficiency = forms.ChoiceField(
        choices=PROFICIENCY_LEVELS,
        widget=forms.RadioSelect,
        required=True,
        label='Proficiency Level'
    )
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Interests'
    )
    domains = forms.ModelMultipleChoiceField(
        queryset=Domain.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Preferred Project Domains'
    )
