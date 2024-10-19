from django.contrib import admin
from .models import TechStack, Interest, Domain, UserSkill, ProjectSuggestion

admin.site.register(TechStack)
admin.site.register(Interest)
admin.site.register(Domain)
admin.site.register(UserSkill)
admin.site.register(ProjectSuggestion)
