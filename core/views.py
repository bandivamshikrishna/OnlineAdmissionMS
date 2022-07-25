from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from exam.models import Course,Result
from student.models import Student, StudentCertificates
from django.contrib.auth.models import User
from .models import *
from .forms import *
from faculty.models import Faculty

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def admin_portal(request):
    return render(request,'core/adminportal.html')

def student_portal(request):
    return render(request,'core/studentportal.html')


def all_course_details(request):
    courses=Course.objects.all()
    return render(request,'core/allcoursedetails.html',{'courses':courses})


def all_faculty_details(request):
    return render(request,'core/allfacultydetails.html')


def course_details(request,id):
    course=Course.objects.get(id=id)
    return render(request,'core/coursedetails.html',{'course':course})

def online_admission(request):
    onlineadmission=OnlineAdmission.objects.get(id=1)
    return render(request,'core/onlineadmission.html',{'onlineadmission':onlineadmission})

def latest_news(request):
    latestnews=LatestNews.objects.get(id=1)
    return render(request,'core/latestnews.html',{'latestnews':latestnews})

def announcements(request):
    announcements=Announcements.objects.get(id=1)
    return render(request,'core/announcements.html',{'announcements':announcements})

def circulars(request):
    circulars=Circulars.objects.get(id=1)
    return render(request,'core/circulars.html',{'circulars':circulars})

def upcoming_events(request):
    upcomingevents=UpcomingEvents.objects.get(id=1)
    return render(request,'core/upcomingevents.html',{'upcomingevents':upcomingevents})

def conferences(request):
    conferences=Conferences.objects.get(id=1)
    return render(request,'core/conferences.html',{'conferences':conferences})

def seminars(request):
    seminars=Seminars.objects.get(id=1)
    return render(request,'core/seminars.html',{'seminars':seminars})

def workshops(request):
    workshops=Workshops.objects.get(id=1)
    return render(request,'core/workshops.html',{'workshops':workshops})

def internships(request):
    internships=Internships.objects.get(id=1)
    return render(request,'core/internships.html',{'internships':internships})



def is_student(user):
    return user.groups.filter(name='STUDENTS').exists()


def is_faculty(user):
    return user.groups.filter(name='FACULTY').exists()

def is_admin(user):
    if user.is_superuser==True:
        return True
    else:
        return False


def afterlogin(request):
    if(is_student(request.user)):
        return HttpResponseRedirect('/student/dashboard/')
    elif (is_faculty(request.user)):
        approved=Faculty.objects.filter(user_id=request.user.id,approved=True)
        if approved: 
            return HttpResponseRedirect('/faculty/dashboard/')
        else:
            return HttpResponseRedirect('/faculty/notapproved/')
    elif (is_admin(request.user)):
        return HttpResponseRedirect('/admin-dashboard/')






#admin module funtionality
def admin_sign_in(request):
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
        return render(request,'admin/signin.html',{'authform':auth_form})
    else:
        return HttpResponseRedirect('/admin-dashboard/')


@login_required(login_url='admin-sign-in')
def admin_dashboard(request):
    return render(request,'admin/dashboard.html')



@login_required(login_url='admin-sign-in')
def admin_online_admission(request):
    data=OnlineAdmission.objects.get(id=1)
    if request.method=='POST':
        form=OnlineAdmissionForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-onlineadmission/')
    else:
        form=OnlineAdmissionForm(instance=data)
    return render(request,'admin/onlineadmission.html',{'form':form,'data':data})



@login_required(login_url='admin-sign-in')
def admin_latest_news(request):
    data=LatestNews.objects.get(id=1)
    if request.method=='POST':
        form=LatestNewsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-latestnews/')
    else:   
        form=LatestNewsForm(instance=data)
    return render(request,'admin/latestnews.html',{'form':form,'data':data})



@login_required(login_url='admin-sign-in')
def admin_announcements(request):
    data=Announcements.objects.get(id=1)
    if request.method=='POST':
        form=AnnouncementsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-announcements/')
    else:
        form=AnnouncementsForm(instance=data)

    return render(request,'admin/announcements.html',{'data':data,'form':form})

@login_required(login_url='admin-sign-in')
def admin_circulars(request):
    data=Circulars.objects.get(id=1)
    if request.method=='POST':
        form=CircularsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-circulars/')
    else:
        form=CircularsForm(instance=data)
    return render(request,'admin/circulars.html',{'form':form,'data':data})

@login_required(login_url='admin-sign-in')
def admin_upcoming_events(request):
    data=UpcomingEvents.objects.get(id=1)
    if request.method=='POST':
        form=UpcomingEventsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-upcomings-events/')
    else:
        form=UpcomingEventsForm(instance=data)
    return render(request,'admin/upcomingevents.html',{'form':form,'data':data})



@login_required(login_url='admin-sign-in')
def admin_conferences(request):
    data=Conferences.objects.get(id=1)
    if request.method=='POST':
        form=ConferencesForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-conferences/')
    else:
        form=ConferencesForm(instance=data)
    return render(request,'admin/conferences.html',{'form':form,'data':data})


@login_required(login_url='admin-sign-in')
def admin_seminars(request):
    data=Seminars.objects.get(id=1)
    if request.method=='POST':
        form=SeminarsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-seminars/')
    else:
        form=SeminarsForm(instance=data)
    return render(request,'admin/seminars.html',{'form':form,'data':data})

@login_required(login_url='admin-sign-in')
def admin_workshops(request):
    data=Workshops.objects.get(id=1)
    if request.method=='POST':
        form=WorkshopsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-workshops/',{'form':form,'data':data})
    else:
        form=WorkshopsForm(instance=data)
    return render(request,'admin/workshops.html',{'data':data,'form':form})

@login_required(login_url='admin-sign-in')
def admin_internships(request):
    data=Internships.objects.get(id=1)
    if request.method=='POST':
        form=InternshipsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-internships/')
    else:
        form=InternshipsForm(instance=data)
    return render(request,'admin/internships.html',{'form':form,'data':data})



@login_required(login_url='admin-sign-in')
def admin_approved_faculty(request):
    facultys=Faculty.objects.filter(approved=True)
    return render(request,'admin/approvedfaculty.html',{'facultys':facultys})



@login_required(login_url='admin-sign-in')
def admin_pending_faculty(request):
    facultys=Faculty.objects.filter(approved=False)
    return render(request,'admin/pendingfaculty.html',{'facultys':facultys})


@login_required(login_url='admin-sign-in')
def admin_approving_faculty(request,id):
    faculty=Faculty.objects.get(id=id)
    faculty.approved=True
    faculty.save()
    return HttpResponseRedirect('/admin-approved-faculty/')

@login_required(login_url='admin-sign-in')
def admin_rejecting_faculty(request,id):
    faculty=Faculty.objects.get(id=id)
    user=User.objects.get(id=faculty.user_id)
    faculty.delete()
    user.delete()
    return HttpResponseRedirect('/admin-pending-faculty/')



@login_required(login_url='admin-sign-in')
def admin_student_details(request):
    students=Result.objects.filter(marks__gt=14)
    return render(request,'admin/studentdetails.html',{'students':students})


@login_required(login_url='admin-sign-in')
def admin_view_certificates(request,id):
    student=Result.objects.get(id=id)
    student_certificates=StudentCertificates.objects.get(student=student.student)
    return render(request,'admin/viewcertificates.html',{'studentcertificates':student_certificates})



@login_required(login_url='admin-sign-in')
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/admin-signin/') 


