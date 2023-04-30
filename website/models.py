from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=100)
    user_message=models.CharField(max_length=500)
    date=models.DateField()

    def __str__(self):
        return self.user_name
    
    