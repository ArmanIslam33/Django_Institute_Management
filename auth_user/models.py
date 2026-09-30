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
    
    
class BaseInfo(models.Model):
    name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=250,null=True)
    phone = models.CharField(max_length=15,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
     
    

