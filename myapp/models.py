from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class register_user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='student_profiles/%Y/%m/%d',null=True, blank=True)
    branch = models.CharField(max_length=256,null=True,blank=True)
    age = models.CharField(max_length=256,null=True,blank=True)
    dob = models.CharField(max_length=256,null=True,blank=True)
    city = models.CharField(max_length=256,blank=True,null=True)
    contect_number = models.CharField(max_length=256,blank=True,null=True)
    gender = models.CharField(max_length=256,null=True,blank=True)
    sports_activity = models.CharField(max_length=256,null=True,blank=True)
    culture_activity = models.CharField(max_length=256,null=True,blank=True)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)




    def __str__(self):
        return self.user.username


class contactForm(models.Model):
    fname = models.CharField(max_length=256)
    lname = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    mn = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.fname