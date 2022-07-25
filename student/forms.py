from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student,StudentCertificates
from exam.models import Course

class StudentUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['address','contact','profile_pic']


class StudentUserFormUpdate(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']


class StudentFormUpdate(forms.ModelForm):
    class Meta:
        model=Student
        fields=['contact','address','profile_pic']



class StudentCertificatesForm(forms.ModelForm):
    class Meta:
        model=StudentCertificates
        fields=['full_name','permanent_address','aadhar','ssc_memo','ssc_bonafide','inter_memo','inter_bonafide','transfer_certificate','caste_certificate','income_certificate','gap_certificate']