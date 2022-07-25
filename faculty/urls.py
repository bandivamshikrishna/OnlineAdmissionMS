from django.urls import path
from .import views


urlpatterns = [
    path('signup/',views.faculty_sign_up,name='faculty-sign-up'),
    path('signin/',views.faculty_sign_in,name='faculty-sign-in'),
    path('notapproved/',views.faculty_not_approved,name='faculty-not-approved'),
    path('dashboard/',views.faculty_dashboard,name='faculty-dashboard'),
    path('profile/',views.faculty_profile,name='faculty-profile'),
    path('addquestion/',views.faculty_add_question,name='faculty-add-question'),
    path('viewquestions/',views.faculty_view_questions,name='faculty-view-questions'),
    path('questionedit/<int:id>/',views.faculty_edit_question,name='faculty-question-edit'),
    path('questiondelete/<int:id>/',views.faculty_delete_question,name='faculty-question-delete'),
    path('editprofile/',views.faculty_edit_profile,name='faculty-edit-profile'),
    path('changepassword/',views.faculty_change_password,name='faculty-change-password'),
    path('logout/',views.faculty_logout,name='faculty-logout'),
]
