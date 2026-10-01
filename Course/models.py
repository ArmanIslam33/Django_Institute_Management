from django.db import models
from auth_user.models import *


# Create your models here.
class CourseCategoryModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    
    
    
class CourseModel(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    course_module = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='./media/CourseImages/',null=True)
    course_fee = models.FloatField(null=True)
    category = models.ForeignKey(
        CourseCategoryModel,
        on_delete=models.SET_NULL,
        related_name='course_category',
        null=True
    )
    duration = models.CharField(max_length=50,null=True)
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        related_name='course_creator',
        null=True
    )
    
    def __str__(self):
        return self.title
    
    