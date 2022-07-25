from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Faculty


class FacultyUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']


class FacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields=['contact','address','profile_pic']


class FacultyUserFormUpdate(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']

class FacultyFormUpdate(forms.ModelForm):
    class Meta:
        model=Faculty
        fields=['address','contact','profile_pic']