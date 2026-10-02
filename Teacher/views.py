from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from auth_user.models import UserModel
from django.contrib import messages
from .forms import *

def teachers_page(request):
    
    datas = TeacherModel.objects.all()
    
    
    return render(request,'teacher/teacher.html',{'datas' : datas})


def add_teacher_page(request):
    
    form_data = TeacherForm()
    
    if request.method == 'POST':
        form_data = TeacherForm(request.POST,request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Teachers Data Created Successfully!')
            return redirect('teachers_page')
    
    
    
    context = {
        'form_data' : form_data,
        'title' : 'Add Teacher Form',
        'heading' : 'Add Teacher Form Page!',
        'btn' : 'Add Teacher'
    }
    
    return render(request,'master/base_form.html',context)

def update_teacher_page(request,id):
    
    data = TeacherModel.objects.get(id=id)
    
    form_data = TeacherForm(instance=data)
    
    if request.method == 'POST':
        form_data = TeacherForm(request.POST,request.FILES,instance=data)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Teachers Data Updated Successfully!')
            return redirect('teachers_page')
    
    
    
    context = {
        'form_data' : form_data,
        'title' : 'Update Teacher Form',
        'heading' : 'Update Teacher Form Page!',
        'btn' : 'Update Teacher'
    }
    
    return render(request,'master/base_form.html',context)


def delete_teacher_page(request,id):
    
    data = TeacherModel.objects.get(id=id)
    data.delete()
    messages.success(request,'Teachers Data Deleted Successfully!')
    return redirect('teachers_page')