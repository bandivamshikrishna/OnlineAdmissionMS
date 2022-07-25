from django.db import models
from student.models import Student
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    abbreviation=models.CharField(max_length=600,null=True)
    course_information=models.TextField(null=True)
    no_of_questions=models.PositiveIntegerField()
    marks=models.PositiveIntegerField()

answer_choices=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    question=models.CharField(max_length=1000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100,choices=answer_choices)
    marks=models.PositiveIntegerField()


class Result(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    marks=models.PositiveIntegerField()
    date=models.DateTimeField(auto_now=True)
