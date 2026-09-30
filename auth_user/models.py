from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    
    USER_TYPE = [
        ('Admin','Admin'),
        ('Student','Student'),
        ('Teacher','Teacher'),
    ]
    
    user_type = models.CharField(choices=USER_TYPE,max_length=50,null=True)

    def __str__(self):
        return self.username
    

