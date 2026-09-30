from django.db import models
from auth_user.models import BaseInfo,UserModel

class StudentModel(BaseInfo):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='student',
        null=True
    )
    image = models.ImageField(upload_to='./media/StudentsImages/',null=True)
    roll_no = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.name
    
