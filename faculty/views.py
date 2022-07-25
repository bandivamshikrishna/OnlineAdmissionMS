from django.shortcuts import render,HttpResponseRedirect
from .forms import FacultyForm,FacultyUserForm,FacultyUserFormUpdate,FacultyFormUpdate
from django.contrib.auth.models import Group,User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from exam.models import Course,Question
from exam.forms import QuestionForm
from .models import Faculty



# Create your views here.
def faculty_sign_up(request):
    courses=Course.objects.all()
    if request.method=='POST':
        course=request.POST.getlist('courses')[0]
        faculty_form=FacultyForm(request.POST,request.FILES)
        user_form=FacultyUserForm(request.POST)
        if faculty_form.is_valid() and user_form.is_valid():
            user=user_form.save()
            faculty=faculty_form.save(commit=False)
            faculty.user=user
            faculty.course=course
            faculty.save()
            faculty_group,created=Group.objects.get_or_create(name='FACULTY')
            user.groups.add(faculty_group)
            return HttpResponseRedirect('/faculty/signin/')
    else:
        faculty_form=FacultyForm()
        user_form=FacultyUserForm()
    return render(request,'faculty/signup.html',{'facultyform':faculty_form,'userform':user_form,'courses':courses})



def faculty_sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            auth_form=AuthenticationForm(request=request,data=request.POST)
            if auth_form.is_valid():
                username=auth_form.cleaned_data.get('username')
                password=auth_form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/afterlogin/')
        else:
            auth_form=AuthenticationForm()
        return render(request,'faculty/signin.html',{'authform':auth_form})
    else:
        return HttpResponseRedirect('/faculty/dashboard/')

def faculty_not_approved(request):
    return render(request,'faculty/notapproved.html')

@login_required(login_url='faculty-sign-in')
def faculty_dashboard(request):
    faculty=Faculty.objects.get(user=request.user)
    return render(request,'faculty/dashboard.html',{'faculty':faculty})



@login_required(login_url='faculty-sign-in')
def faculty_profile(request):
    faculty=Faculty.objects.get(user=request.user)
    user=User.objects.get(id=faculty.user_id)
    return render(request,'faculty/profile.html',{'faculty':faculty,'user':user})



@login_required(login_url='faculty-sign-in')
def faculty_add_question(request):
    faculty=Faculty.objects.get(user=request.user)
    course=faculty.course
    course=Course.objects.get(name=course)
    if request.method=='POST':
        question_form=QuestionForm(request.POST)
        if question_form.is_valid():
            question=question_form.save(commit=False)
            question.course=course
            question.save()
            question_form=QuestionForm()
    else:
        question_form=QuestionForm()
    return render(request,'faculty/addquestion.html',{'questionform':question_form,'course':course})



@login_required(login_url='faculty-sign-in')
def faculty_view_questions(request):
    faculty=Faculty.objects.get(user=request.user)
    course=faculty.course
    course=Course.objects.get(name=course)
    questions=Question.objects.filter(course=course)
    return render(request,'faculty/viewquestions.html',{'questions':questions,'course':course})



@login_required(login_url='faculty-sign-in')
def faculty_edit_question(request,id):
    question=Question.objects.get(id=id)
    if request.method=='POST':
        question_form=QuestionForm(request.POST,instance=question)
        if question_form.is_valid():
            question_form.save()
            return HttpResponseRedirect('/faculty/viewquestions/')
    else:
        question_form=QuestionForm(instance=question)
    return render(request,'faculty/editquestion.html',{'questionform':question_form})



@login_required(login_url='faculty-sign-in')
def faculty_delete_question(request,id):
    question=Question.objects.get(id=id).delete()
    return HttpResponseRedirect('/faculty/viewquestions/') 


@login_required(login_url='faculty-sign-in')
def faculty_edit_profile(request):
    faculty=Faculty.objects.get(user=request.user)
    user=User.objects.get(id=faculty.user_id)
    if request.method=='POST':
        faculty_update_form=FacultyFormUpdate(request.POST,request.FILES,instance=faculty)
        user_update_form=FacultyUserFormUpdate(request.POST,instance=user)
        if faculty_update_form.is_valid() and user_update_form.is_valid():
            user=user_update_form.save()
            faculty=faculty_update_form.save(commit=False)
            faculty.user=user
            faculty.save()
            return HttpResponseRedirect('/faculty/profile/')
    else:
        faculty_update_form=FacultyFormUpdate(instance=faculty)
        user_update_form=FacultyUserFormUpdate(instance=user)
    return render(request,'faculty/editprofile.html',{'facultyupdateform':faculty_update_form,'userupdateform':user_update_form,'faculty':faculty})


@login_required(login_url='faculty-sign-in')
def faculty_change_password(request):
    if request.method=='POST':
        password_form=PasswordChangeForm(user=request.user,data=request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request,password_form.user)
            return HttpResponseRedirect('/faculty/profile/')
    else:
        password_form=PasswordChangeForm(user=request.user)
    return render(request,'faculty/changepassword.html',{'passwordform':password_form})



@login_required(login_url='faculty-sign-in')
def faculty_logout(request):
    logout(request)
    return HttpResponseRedirect('/faculty/signin/') 