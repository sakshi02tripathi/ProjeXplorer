from django.db import models
from django.contrib.auth.models import User

# Model to represent different programming languages or technologies
class TechStack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model to represent user interests
class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model to represent project domains (areas of focus)
class Domain(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Choice options for proficiency levels
PROFICIENCY_LEVELS = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
]

# Model to represent each user's skills in a specific tech stack and their proficiency level
class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Connects to the user who owns the skill
    tech_stack = models.ForeignKey(TechStack, on_delete=models.CASCADE)  # Links to the tech stack
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS)  # Select proficiency level

    def __str__(self):
        return f"{self.user.username} - {self.tech_stack.name} ({self.proficiency})"

# Model to represent the project suggestions
class ProjectSuggestion(models.Model):
    name = models.CharField(max_length=200)  # Name of the project
    description = models.TextField()  # Description of the project
    required_tech_stacks = models.ManyToManyField(TechStack)  # Required tech stacks for this project
    related_domains = models.ManyToManyField(Domain)  # Related project domains
    interests = models.ManyToManyField(Interest)  # Interests related to the project

    def __str__(self):
        return self.name
