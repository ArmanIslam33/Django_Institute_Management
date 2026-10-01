from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def course_category(request):
    
    datas = CourseCategoryModel.objects.all()
    
    context = {
        'datas' : datas
    }
    
    return render(request,'course/courseCategory.html',context)


def add_course_category(request):
    
    form_data = CourseCategoryForm()
    
    if request.method == 'POST':
        form_data = CourseCategoryForm(request.POST)
        
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Course Category Created Successfully!')
            return redirect('course_category')
    
    
    context = {
        'form_data' : form_data,
        'title' : 'Add Course Category',
        'heading' : 'Add Course Category Page!',
        'btn' : 'Add Category'
    }
    
    return render(request,'master/base_form.html',context)

def update_course_category(request,id):
    
    data = get_object_or_404(CourseCategoryModel,id=id)
    
    form_data = CourseCategoryForm(instance=data)
    
    if request.method == 'POST':
        form_data = CourseCategoryForm(request.POST,instance=data)
        
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Course Category Updated Successfully!')
            return redirect('course_category')
    
    
    context = {
        'form_data' : form_data,
        'title' : 'Update Course Category',
        'heading' : 'Update Course Category Page!',
        'btn' : 'Update Category'
    }
    
    return render(request,'master/base_form.html',context)

def delete_course_category(request,id):
    
    data = get_object_or_404(CourseCategoryModel,id=id)
    data.delete()
    messages.success(request,'Course Category Deleted Successfully!')
    return redirect('course_category')
