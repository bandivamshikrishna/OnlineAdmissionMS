from django.contrib import admin
from .models import Conferences, OnlineAdmission,Seminars,Workshops,UpcomingEvents,Internships,LatestNews,Announcements,Circulars

# Register your models here.
@admin.register(OnlineAdmission)
class OnlineAdmissionAdmin(admin.ModelAdmin):
    list_display=['id','onlineadmission','pic1','pic2']


@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display=['id','latestnews']


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display=['id','announcements']


@admin.register(Circulars)
class CircularAdmin(admin.ModelAdmin):
    list_display=['id','pic1']



@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display=['id','upcoming_events']


@admin.register(Conferences)
class ConferencesAdmin(admin.ModelAdmin):
    list_display=['id','conferences']



@admin.register(Seminars)
class SeminarsAdmin(admin.ModelAdmin):
    list_display=['id','seminars','pic1','pic2','pic3','pic4']

@admin.register(Workshops)
class WorkshopsAdmin(admin.ModelAdmin):
    list_display=['id','workshops','pic1','pic2','pic3','pic4']



@admin.register(Internships)
class InternshipsAdmin(admin.ModelAdmin):
    list_display=['id','internships']

