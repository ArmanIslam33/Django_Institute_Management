from django.db import models
from auth_user.models import BaseInfo,UserModel
from Course.models import CourseModel

class TeacherModel(BaseInfo):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='teacher',
        null=True,
    )
    subject = models.ForeignKey(
        CourseModel,
        on_delete=models.SET_NULL,
        related_name='teachers_subject',
        null = True,
        blank = True
    )
    joining_date = models.DateField(null=True)
    image = models.ImageField(upload_to='./media/TeachersImages/',null=True)

    def __str__(self):
        return self.name
    