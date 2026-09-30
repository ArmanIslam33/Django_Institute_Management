from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def studentPage(request):
    
    student_datas = StudentModel.objects.all()
    
    context = {
        'student_datas' : student_datas
    }
    
    return render(request,'student/student.html',context)

def addStudentPage(request):
    
    form_data = StudentForm()
    
    if request.method == 'POST':
        form_data = StudentForm(request.POST,request.FILES)
        
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Student Account Created Successfully!')
            return redirect('studentPage')
    
    
    context = {
        'form_data' : form_data,
        'title' : 'Add Student Form',
        'heading' : 'Add Student Form Page!',
        'btn' : 'Add Student'
    }
    
    return render(request,'master/base_form.html',context)
