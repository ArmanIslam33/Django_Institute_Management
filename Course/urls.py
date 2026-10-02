from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    # ------ Course Category
    path('course_category/',course_category,name='course_category'),
    path('add_course_category/',add_course_category,name='add_course_category'),
    path('update_course_category/<str:id>/',update_course_category,name='update_course_category'),
    path('delete_course_category/<str:id>/',delete_course_category,name='delete_course_category'),
    
    
    # ========= Course Pages
    path('course_page/',course_page,name='course_page'),
    path('add_course/',add_course,name='add_course'),
    path('update_course/<str:id>/',update_course,name='update_course'),
    path('delete_course/<str:id>/',delete_course,name='delete_course'),

    
]
