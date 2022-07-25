from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    contact=models.PositiveIntegerField()
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile_pic/student/',null=False,blank=False)
    course=models.CharField(max_length=40,null=True)
    certificates_uploaded=models.BooleanField(default=False,null=True)


class StudentCertificates(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=400)
    permanent_address=models.CharField(max_length=4000,null=True)
    aadhar=models.ImageField(upload_to='certificates/')
    ssc_memo=models.ImageField(upload_to='certificates/')
    ssc_bonafide=models.ImageField(upload_to='certificates/')
    inter_memo=models.ImageField(upload_to='certificates/')
    inter_bonafide=models.ImageField(upload_to='certificates/')
    transfer_certificate=models.ImageField(upload_to='certificates/')
    caste_certificate=models.ImageField(upload_to='certificates/')
    income_certificate=models.ImageField(upload_to='certificates/')
    gap_certificate=models.ImageField(upload_to='certificates/',null=True,blank=True)
    