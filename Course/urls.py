from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('course_category/',course_category,name='course_category'),
    path('add_course_category/',add_course_category,name='add_course_category'),
    path('update_course_category/<str:id>/',update_course_category,name='update_course_category'),
    path('delete_course_category/<str:id>/',delete_course_category,name='delete_course_category'),
]
