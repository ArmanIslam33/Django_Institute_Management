from django.urls import path
from .views import *

urlpatterns = [
    path('teachers_page/', teachers_page, name='teachers_page'),
    path('add_teacher_page/', add_teacher_page, name='add_teacher_page'),
    path('update_teacher_page/<str:id>/', update_teacher_page, name='update_teacher_page'),
    path('delete_teacher_page/<str:id>/', delete_teacher_page, name='delete_teacher_page'),
]
