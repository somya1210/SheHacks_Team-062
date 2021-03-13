from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __str__(self):
        return self.title
