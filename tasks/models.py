from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(primary_key=True, max_length=100)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
