from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User, default=None,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'