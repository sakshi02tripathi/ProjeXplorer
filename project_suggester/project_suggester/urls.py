from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from suggester import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),  # Added signup view
    path('login/', auth_views.LoginView.as_view(template_name='suggester/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('skill-input/', views.skill_input_view, name='skill_input'),
    path('suggestions/', views.project_suggestions_view, name='project_suggestions'),
    path('', views.home_redirect, name='home_redirect'),  # Redirect root URL
]

