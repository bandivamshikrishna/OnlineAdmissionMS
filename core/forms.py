from django import forms
from .models import OnlineAdmission,LatestNews,Announcements,Circulars,UpcomingEvents,Conferences,Seminars,Workshops,Internships

class OnlineAdmissionForm(forms.ModelForm):
    class Meta:
        model=OnlineAdmission
        fields=['onlineadmission','pic1','pic2']


class LatestNewsForm(forms.ModelForm):
    class Meta:
        model=LatestNews
        fields=['latestnews','pic1','pic2']



class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model=Announcements
        fields=['announcements','pic1','pic2']

class CircularsForm(forms.ModelForm):
    class Meta:
        model=Circulars
        fields=['pic1']


class UpcomingEventsForm(forms.ModelForm):
    class Meta:
        model=UpcomingEvents
        fields=['upcoming_events']


class ConferencesForm(forms.ModelForm):
    class Meta:
        model=Conferences
        fields=['conferences','pic1','pic2']


class SeminarsForm(forms.ModelForm):
    class Meta:
        model=Seminars
        fields=['seminars','pic1','pic2','pic3','pic4']


class WorkshopsForm(forms.ModelForm):
    class Meta:
        model=Workshops
        fields=['workshops','pic1','pic2','pic3','pic4']


class InternshipsForm(forms.ModelForm):
    class Meta:
        model=Internships
        fields=['internships']