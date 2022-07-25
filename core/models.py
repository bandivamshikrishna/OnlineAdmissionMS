from django.db import models

# Create your models here.
class OnlineAdmission(models.Model):
    onlineadmission=models.TextField()
    pic1=models.ImageField(upload_to='core/',null=True)
    pic2=models.ImageField(upload_to='core/',null=True)

class LatestNews(models.Model):
    latestnews=models.TextField()
    pic1=models.ImageField(upload_to='core/',null=True)
    pic2=models.ImageField(upload_to='core/',null=True)


class Announcements(models.Model):
    announcements=models.TextField()
    pic1=models.ImageField(upload_to='core/',null=True)
    pic2=models.ImageField(upload_to='core/',null=True)


class Circulars(models.Model):
    pic1=models.ImageField(upload_to='core/',null=True)

class UpcomingEvents(models.Model):
    upcoming_events=models.TextField()

class Conferences(models.Model):
    conferences=models.TextField()
    pic1=models.ImageField(upload_to='core/',null=True)
    pic2=models.ImageField(upload_to='core/',null=True)


class Seminars(models.Model):
    seminars=models.TextField()
    pic1=models.ImageField(upload_to='core/',null=True)
    pic2=models.ImageField(upload_to='core/',null=True)
    pic3=models.ImageField(upload_to='core/',null=True)
    pic4=models.ImageField(upload_to='core/',null=True)

class Workshops(models.Model):
    workshops=models.TextField()
    pic1=models.ImageField(upload_to='core/',null=True)
    pic2=models.ImageField(upload_to='core/',null=True)
    pic3=models.ImageField(upload_to='core/',null=True)
    pic4=models.ImageField(upload_to='core/',null=True)

class Internships(models.Model):
    internships=models.TextField()

