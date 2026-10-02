from django import forms
from auth_user.models import UserModel
from .models import *
from django.db import transaction

class TeacherForm(forms.ModelForm):
    
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    
    class Meta:
        model = TeacherModel
        fields = ['name','username', 'email' ,'phone','subject','address','joining_date','image']
        exclude = ['user']
        
        widgets = {
            'joining_date' : forms.DateInput(attrs={
                'type' : 'date'
            })
        }
        
    @transaction.atomic   
    def save(self, commit = True):
        
        user = UserModel.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='12345',
            user_type='Teacher'
        )
        
        teacher = super().save(commit=False)
        teacher.user = user
        if commit:
            teacher.save()
        return teacher
        