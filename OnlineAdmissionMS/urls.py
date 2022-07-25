"""OnlineAdmissionMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('student_portal/',views.student_portal,name='student-portal'),
    path('adminportal/',views.admin_portal,name='admin-portal'),
    path('allcoursedetails/',views.all_course_details,name='all-course-details'),
    path('allfacultydetails/',views.all_faculty_details,name='all-faculty-details'),
    path('coursedetails/<int:id>/',views.course_details,name='course-details'),
    path('onlineadmission/',views.online_admission,name='online-admission'),
    path('latestnews/',views.latest_news,name='latest-news'), 
    path('announcements/',views.announcements,name='announcements'),
    path('circulars/',views.circulars,name='circulars'),
    path('upcomingsevents/',views.upcoming_events,name='upcoming-events'),
    path('conferences/',views.conferences,name='conferences'),
    path('seminars/',views.seminars,name='seminars'),
    path('workshops/',views.workshops,name='workshops'),
    path('internships/',views.internships,name='internships'),
    path('afterlogin/',views.afterlogin,name='after-login'),



    #admin urls
    path('admin-signin/',views.admin_sign_in,name='admin-sign-in'),
    path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
    path('admin-onlineadmission/',views.admin_online_admission,name='admin-online-admission'),
    path('admin-latestnews/',views.admin_latest_news,name='admin-latest-news'),
    path('admin-announcements/',views.admin_announcements,name='admin-announcements'),
    path('admin-circulars/',views.admin_circulars,name='admin-circulars'),
    path('admin-upcomings-events/',views.admin_upcoming_events,name='admin-upcoming-events'),
    path('admin-conferences/',views.admin_conferences,name='admin-conferences'),
    path('admin-seminars/',views.admin_seminars,name='admin-seminars'),
    path('admin-workshops/',views.admin_workshops,name='admin-workshops'),
    path('admin-internships/',views.admin_internships,name='admin-internships'),
    path('admin-approved-faculty/',views.admin_approved_faculty,name='admin-approved-faculty'),
    path('admin-approving-faculty/<int:id>/',views.admin_approving_faculty,name='admin-approving-faculty'),
    path('admin-rejecting-faculty/<int:id>/',views.admin_rejecting_faculty,name='admin-rejecting-faculty'),
    path('admin-pending-faculty/',views.admin_pending_faculty,name='admin-pending-faculty'),
    path('admin-student-details/',views.admin_student_details,name='admin-student-details'),
    path('admin-view-certificates/<int:id>/',views.admin_view_certificates,name='admin-view-certificates'),
    path('admin-logout/',views.admin_logout,name='admin-logout'),






    path('student/',include('student.urls')),
    path('faculty/',include('faculty.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)