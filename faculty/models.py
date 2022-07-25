from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Faculty(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    contact=models.PositiveIntegerField()
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile_pic/faculty/',null=True)
    course=models.CharField(max_length=40)
    approved=models.BooleanField(default=False)