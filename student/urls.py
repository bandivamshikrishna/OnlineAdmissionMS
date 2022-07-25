from re import U
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.student_sign_up,name='student-sign-up'),
    path('signin/',views.student_sign_in,name='student-sign-in'),
    path('dashboard/',views.student_dashboard,name='student-dashboard'),
    path('logout/',views.student_logout,name='student-logout'),
    path('profile/',views.student_profile,name='student-profile'),
    path('courseselection/',views.student_course_selection,name='student-course-selection'),
    path('taketotest/',views.student_take_to_test,name='student-take-to-test'),
    path('exam/<str:course>/',views.student_exam,name='student-exam'),
    path('calculatemarks/',views.student_calculate_marks,name='student-calculate-marks'),
    path('marksdetails/',views.student_marks_details,name='student-marks-details'),

    path('uploadcertificates/',views.student_upload_certificates,name='student-upload-certificates'),
    path('certificatesuploaded/',views.student_certificates_uploaded,name='student-certificates-uploaded'),
    path('editprofile/',views.student_edit_profile,name='student-edit-profile'),
    path('changepassword/',views.student_change_password,name='student-change-password'),
]
