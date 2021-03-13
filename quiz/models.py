from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    name = models.ForeignKey(User, default=None,on_delete=models.CASCADE, null=False)
    question = models.CharField(max_length=200)
    option_1 = models.IntegerField()
    option_2 = models.IntegerField()
    option_3 = models.IntegerField()
    option_4 = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    
    
