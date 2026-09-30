from django.urls import path
from .views import *

urlpatterns = [
    path('',signInPage,name='signInPage'),
    path('signOutPage/',signOutPage,name='signOutPage'),
    path('dashboard/',dashboardPage,name='dashboardPage'),
]
