from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


def signInPage(request):
    
    form_data = AuthenticationForm()
    
    if request.method == 'POST':
        form_data = AuthenticationForm(request,request.POST)

        if form_data.is_valid():
            login(request,form_data.get_user())
            messages.success(request,'Successfully Logged In!')
            return redirect('dashboardPage')
    
    
    context = {
        'form_data' : form_data
    }
    
    return render(request,'signin.html',context)

@login_required
def signOutPage(request):
    logout(request)
    messages.success(request,'Logged Out')
    return redirect('signInPage')
    

@login_required
def dashboardPage(request):
    
    return render(request,'dashboard.html')
