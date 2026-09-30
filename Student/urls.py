from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('studentPage/',studentPage,name='studentPage'),
    path('addStudentPage/',addStudentPage,name='addStudentPage'),
]
