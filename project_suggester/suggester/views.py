from django.shortcuts import render, redirect
from .forms import SkillForm
from .models import ProjectSuggestion, TechStack, Interest, Domain
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm

def skill_input_view(request):
    if request.method == 'POST':
        # Get user inputs from the form
        selected_tech_stack_ids = request.POST.getlist('tech_stacks')  # List of selected tech stacks
        selected_interests_ids = request.POST.getlist('interests')  # List of selected interests
        selected_domains_ids = request.POST.getlist('domains')  # List of selected domains
        selected_proficiency = request.POST.get('proficiency')  # Selected proficiency


        # Filter projects based on user input
        suggested_projects = ProjectSuggestion.objects.filter(
            required_tech_stacks__id__in=selected_tech_stack_ids,
            interests__in=selected_interests_ids,
            related_domains__in=selected_domains_ids
        ).distinct()

        # Check if any suggestions are found
        if suggested_projects.exists():
            return render(request, 'suggester/project_suggestions.html', {'projects': suggested_projects})
        else:
            return render(request, 'suggester/project_suggestions.html', {'message': 'No project suggestions found based on your input.'})

    # If it's a GET request, render the skill input form
    tech_stacks = TechStack.objects.all()
    interests = Interest.objects.all()
    domains = Domain.objects.all()
    return render(request, 'suggester/skill_form.html', {
        'tech_stacks': tech_stacks,
        'interests': interests,
        'domains': domains
    })

def project_suggestions_view(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            tech_stacks = form.cleaned_data['tech_stacks']
            proficiency = form.cleaned_data['proficiency']
            interests = form.cleaned_data['interests']
            domains = form.cleaned_data['domains']

            # Fetch project suggestions based on the selected inputs
            suggestions = ProjectSuggestion.objects.filter(
                required_tech_stacks__in=tech_stacks,
                related_domains__in=domains,
                interests__in=interests
            ).distinct()

            return render(request, 'suggester/project_suggestions.html', {'suggestions': suggestions})
    else:
        form = SkillForm()

    return render(request, 'suggester/skill_form.html', {'form': form})

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('skill_input')  # Redirect to home if logged in
    return redirect('login')  # Otherwise, go to login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('skill_input')  # Redirect to skill input after signup
    else:
        form = UserCreationForm()
    return render(request, 'suggester/signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':  # Check if it's a POST request
        logout(request)
        return redirect('login')  # Redirect to login page after logout
    return redirect('home')

