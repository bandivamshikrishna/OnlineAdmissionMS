from ast import Pass
from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import Group,User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Student
from exam.models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def student_sign_up(request):
    if request.method=='POST':
        student_form=StudentForm(request.POST,request.FILES)
        user_form=StudentUserForm(request.POST)
        if student_form.is_valid() and user_form.is_valid():
            email=user_form.cleaned_data.get('email')
            username=user_form.cleaned_data.get('username')
            user=user_form.save()
            student=student_form.save(commit=False)
            student.user=user
            student.save()
            subject='Welcome to Tagore Degree College'
            message='''Account has been created :
            TAGORE DEGREE COLLEGE(AUTONOMOUS)
            Mr.'''+username.title()+''' welcome to tagore degree college(autonomous)
            your account has been sucessfully created!.
            we are the providing the online admissions for the courses like 
            BCA,BBA,BCOM.COMPUTERS.BA.BSC.(LIFESCIENCE)
            online Admission process:
            First you need to attempt the  test
            If you qualified the test then you need to  upload the certificates.

            “Education is the most powerful weapon which you can use to change the world.”


            Incase of any queries,please contact the helpline number 7671959015  or 
            write to us at katravathrajendar18@gmail.com

            Regards,
            team TDCA!'''
            student_group,created=Group.objects.get_or_create(name='STUDENTS')
            user.groups.add(student_group)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=True)
            return HttpResponseRedirect('/student/signin/')
    else:
        student_form=StudentForm()
        user_form=StudentUserForm()
    return render(request,'student/signup.html',{'studentform':student_form,'userform':user_form})


def student_sign_in(request):
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
        return render(request,'student/signin.html',{'authform':auth_form})
    else:
        return HttpResponseRedirect('/student/dashboard/')


@login_required(login_url='student-sign-in')
def student_dashboard(request):
    student=Student.objects.get(user=request.user)
    exam_completed=Result.objects.filter(student=student).exists()
    if exam_completed:
        qualified=exam_qualified(request)
        return render(request,'student/dashboard.html',{'student':student,'examcompleted':exam_completed,'qualified':qualified})
    return render(request,'student/dashboard.html',{'student':student})  


@login_required(login_url='student-sign-in')
def student_profile(request):
    student=Student.objects.get(user=request.user)
    user=User.objects.get(id=student.user_id)
    exam_completed=Result.objects.filter(student=student).exists()
    if exam_completed:
        qualified=exam_qualified(request)
        return render(request,'student/profile.html',{'student':student,'examcompleted':exam_completed,'qualified':qualified})
    return render(request,'student/profile.html',{'student':student,'user':user})


def exam_qualified(request):
    student=Student.objects.get(user=request.user)
    result=Result.objects.get(student=student)
    if result.marks>=14:
        return True
    elif result.marks<14:
        return False

@login_required(login_url='student-sign-in')
def student_course_selection(request):
    courses=Course.objects.all()
    student=Student.objects.get(user=request.user)
    if request.method=='POST':
        course=request.POST.getlist('courses')[0]
        student.course=course
        student.save()
        return HttpResponseRedirect('/student/taketotest/') 
    exam_completed=Result.objects.filter(student=student).exists()
    if exam_completed:
        qualified=exam_qualified(request)
        return render(request,'student/courseselection.html',{'student':student,'examcompleted':exam_completed,'qualified':qualified})
    return render(request,'student/courseselection.html',{'courses':courses})



@login_required(login_url='student-sign-in')
def student_take_to_test(request):
    student=Student.objects.get(user=request.user)
    course=Course.objects.get(name=student.course)
    questions=Question.objects.filter(course=course)
    total_marks=0
    for question in questions:
        total_marks=question.marks+total_marks
    exam_completed=Result.objects.filter(student=student).exists()
    
    if exam_completed:
        qualified=exam_qualified(request)
        return render(request,'student/taketotest.html',{'student':student,'examcompleted':exam_completed,'questions':questions,'totalmarks':total_marks,'qualified':qualified})
    return render(request,'student/taketotest.html',{'student':student,'questions':questions,'totalmarks':total_marks})



@login_required(login_url='student-sign-in')
def student_exam(request,course):
    student=Student.objects.get(user=request.user)
    qcourse=Course.objects.get(name=course)
    questions=Question.objects.filter(course=qcourse)
    exam_completed=Result.objects.filter(student=student).exists()
    if exam_completed:
        qualified=exam_qualified(request)
        return render(request,'student/exam.html',{'student':student,'examcompleted':exam_completed,'course':qcourse,'questions':questions,'qualified':qualified})
    if request.method=='POST':
        pass
    response=render(request,'student/exam.html',{'course':qcourse,'questions':questions})
    response.set_cookie('student_object_number_course_exam',str(student)+' '+str(course)+' '+'exam')
    return response



@login_required(login_url='student-sign-in')
def student_calculate_marks(request): 
    if request.COOKIES.get('student_object_number_course_exam') is not None:
        student,object,number,course_name,exam=request.COOKIES.get('student_object_number_course_exam').split()
        course=Course.objects.get(name=course_name)
        total_marks=0
        questions=Question.objects.all().filter(course=course)
        for i in range(len(questions)):
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            selected_ans=selected_ans.lower()
            actual_answer=actual_answer.lower()
            if selected_ans==actual_answer:
                total_marks = total_marks + questions[i].marks
        student = Student.objects.get(user_id=request.user.id)
        result = Result(student=student,course=course,marks=total_marks)
        result.save()
        date=result.date
        user=User.objects.get(id=request.user.id)
        username=user.username
        email=user.email
        subject='Welcome to Tagore Degree College'
        if result.marks>14:
           
            message='''TAGORE DEGREE COLLEGE(AUTONOMOUS)
            Congrualtions Mr.'''+username+'''

            you have attempted the test at   '''+str(date)+'''\n
            Thanks for participating in online admission test in tagore degree college.we are happy to inform that your selected for the admission process for   '''+course_name+''' course
            In order to confirm your  admssion process please  upload the certificates .
            Incase of any queries,please contact the helpline number 7671959015  or write to us at katravathrajendar18@gmail.com
            Regards,
            team TDCA!'''
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=True)
        elif result.marks<14:
            message='''Hello Mr.'''+username.title()+'''
            you have attempted the test at  '''+str(date)+'''\n
            We regret to inform you that you were unable to clear the online admission test for bca course.

            While you would not be eligible to join the upcoming batch at TAGORE DEGREE COLLEGE(AUTONOMOUS) , this is not the end of the line for you.
            We will inform you by email when our next batch admissions are open!
            In case of any queries,please contact the college helpline number 7671959015 or write to us at katravathrajendar18@gmail.com.
            Regrads,
            team TDCA!'''
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=True)
            
        return HttpResponseRedirect('/student/marksdetails/')




@login_required(login_url='student-sign-in')
def student_marks_details(request):
    student=Student.objects.get(user=request.user)
    result=Result.objects.get(student=student)
    exam_qualification=None
    if result.marks>=14:
        exam_qualification='yes'
    elif result.marks<14:
        exam_qualification='no'
    exam_completed=Result.objects.filter(student=student).exists()
    if exam_completed:
        qualified=exam_qualified(request)
        return render(request,'student/marksdetails.html',{'student':student,'examcompleted':exam_completed,'result':result,'student':student,'qualified':qualified,'examqualification':exam_qualification})
    return render(request,'student/marksdetails.html',{'result':result,'student':student,'examqualification':exam_qualification})



@login_required(login_url='student-sign-in')
def student_upload_certificates(request):
    student=Student.objects.get(user=request.user)
    result=Result.objects.get(student=student)
    if request.method=='POST':
        certificate_form=StudentCertificatesForm(request.POST,request.FILES)
        if certificate_form.is_valid():
            full_name=certificate_form.cleaned_data.get('full_name')
            permanent_address=certificate_form.cleaned_data.get('permanent_address')
            aadhar=certificate_form.cleaned_data.get('aadhar')
            ssc_memo=certificate_form.cleaned_data.get('ssc_memo')
            ssc_bonafide=certificate_form.cleaned_data.get('ssc_bonafide')
            inter_memo=certificate_form.cleaned_data.get('inter_memo')
            inter_bonafide=certificate_form.cleaned_data.get('inter_bonafide')
            transfer_certificate=certificate_form.cleaned_data.get('transfer_certificate')
            caste_certificate=certificate_form.cleaned_data.get('caste_certificate')
            income_certificate=certificate_form.cleaned_data.get('income_certificate')
            gap_certificate=None
            if certificate_form.cleaned_data.get('gap_certificate'):
                gap_certificate=certificate_form.cleaned_data.get('gap_certificate')
            student_certificates=StudentCertificates(student=student,full_name=full_name,permanent_address=permanent_address,aadhar=aadhar,ssc_memo=ssc_memo,ssc_bonafide=ssc_bonafide,inter_memo=inter_memo,inter_bonafide=inter_bonafide,transfer_certificate=transfer_certificate,caste_certificate=caste_certificate,income_certificate=income_certificate,gap_certificate=gap_certificate)
            student.certificates_uploaded=True
            student.save()
            student_certificates.save()
            return HttpResponseRedirect('/student/certificatesuploaded/')
    else:
        exam_completed=Result.objects.filter(student=student).exists()
        if exam_completed:
            qualified=exam_qualified(request)
            if qualified:
                certificate_form=StudentCertificatesForm()
                certificates_uploaded=StudentCertificates.objects.filter(student=student).exists()
                if certificates_uploaded:
                    return HttpResponseRedirect('/student/certificatesuploaded/')
                return render(request,'student/uploadcertificates.html',{'student':student,'examcompleted':exam_completed,'qualified':qualified,'certificateform':certificate_form})
            else:
                return HttpResponseRedirect('/student/profile/')
    



@login_required(login_url='student-sign-in')
def student_certificates_uploaded(request):
    student=Student.objects.get(user=request.user)
    exam_completed=Result.objects.filter(student=student).exists()
    if exam_completed:
        qualified=exam_qualified(request)
        return render(request,'student/certificatesuploaded.html',{'examcompleted':exam_completed,'qualified':qualified})




@login_required(login_url='student-sign-in')
def student_edit_profile(request):
    student=Student.objects.get(user=request.user)
    user=User.objects.get(id=student.user_id)
    if request.method=='POST':
        student_update_form=StudentFormUpdate(request.POST,request.FILES,instance=student)
        user_update_form=StudentUserFormUpdate(request.POST,instance=user)
        if student_update_form.is_valid() and user_update_form.is_valid():
            user=user_update_form.save()
            student=student_update_form.save(commit=False)
            student.user=user
            student.save()
            return HttpResponseRedirect('/student/profile/')
    else:
        student_update_form=StudentFormUpdate(instance=student)
        user_update_form=StudentUserFormUpdate(instance=user)
        exam_completed=Result.objects.filter(student=student).exists()
        if exam_completed:
            qualified=exam_qualified(request)
            return render(request,'student/editprofile.html',{'student':student,'examcompleted':exam_completed,'studentupdateform':student_update_form,'userupdateform':user_update_form,'student':student,'qualified':qualified})
    return render(request,'student/editprofile.html',{'studentupdateform':student_update_form,'userupdateform':user_update_form,'student':student})



@login_required(login_url='student-sign-in')
def student_change_password(request):
    student=Student.objects.get(user=request.user)
    if request.method=='POST':
        password_form=PasswordChangeForm(user=request.user,data=request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request,password_form.user)
            return HttpResponseRedirect('/student/profile/')
    else:
        password_form=PasswordChangeForm(user=request.user)
        exam_completed=Result.objects.filter(student=student).exists()
        if exam_completed:
            qualified=exam_qualified(request)
            return render(request,'student/changepassword.html',{'student':student,'examcompleted':exam_completed,'passwordform':password_form,'qualified':qualified})
    return render(request,'student/changepassword.html',{'passwordform':password_form})



@login_required(login_url='student-sign-in')
def student_logout(request):
    logout(request)
    return HttpResponseRedirect('/student/signin/')