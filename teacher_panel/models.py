from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class teacher_detailes(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='teachers_profiles/%Y/%m/%d',blank=True,null=True)
    subject = models.CharField(max_length=256,null=True,blank=True)
    dob = models.CharField(max_length=256,null=True,blank=True)
    city = models.CharField(max_length=256,blank=True,null=True)
    contect_number = models.CharField(max_length=256,blank=True,null=True)
    gender = models.CharField(max_length=256,null=True,blank=True)


    def __str__(self):
        return self.user.username


class add_photos(models.Model):
    title = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='Gallary/%Y/%m/%d',blank=True,null=True)
    catagory = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class add_notification(models.Model):
    title_notification = models.CharField(max_length=256)
    photo_notification = models.ImageField(upload_to='notification/%Y/%m/%d',blank=True,null=True)
    notification = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)

    def get_date(self):
        time = datetime.now()
        if self.date.hour == time.hour:
            return str(time.minute - self.date.minute) + "minutes ago"
        elif self.date.day == time.day:
            return str(time.hour - self.date.hour) + " hours ago"

        elif self.date.month == time.month:
            return str(time.day - self.date.day) + " days ago"

        else:
            if self.created_at.year == time.year:
                return str(time.month - self.created_at.month) + " months ago"

        return self.date

    def __str__(self):
        return self.title_notification
          
