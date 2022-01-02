from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from teacher_panel import models
from teacher_panel.models import teacher_detailes,add_photos,add_notification
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def teacher_dashboard(request):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data
    return render(request,'teacher_panel/dashboard.html',context)


@login_required
def teacher_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



@login_required
def edit_teacher_profile(request):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data
    if request.method == "POST":
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        subject = request.POST['subject']
        dob = request.POST['dob']
        city = request.POST['city']
        gender = request.POST['gender']
        cn = request.POST['cn']

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()


        data.subject = subject
        data.dob = dob
        data.city = city
        data.contect_number = cn
        data.gender = gender
        data.save()

        if 'image' in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()

        
    context['status'] = "You Update Your Profile Successfully"
    return render(request,'teacher_panel/edit_teacher_profile.html',context)



@login_required
def change_teacher_password(request):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data

    if request.method == "POST":
        current = request.POST["password"]
        new_password = request.POST["new_password"]

        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_password)
            user.save()
            context["message"] = "Your Password is Changed Successfully"
            context["col"] = "alert alert-success"
            user = User.objects.get(username=un)
            login(request,user)
        else:
            context["message"] = "Incorrect Current Password"
            context["col"] = "alert alert-danger"
    return render(request, 'teacher_panel/change_teacher_password.html',context)


@login_required
def delete_teacher_profile(request):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data
    return render(request,'teacher_panel/delete_teacher_profile.html',context)


@login_required
def confirm_teacher_delete(request):
    user = User.objects.get(id = request.user.id)
    user.delete()
    return redirect("/")

@login_required
def student_list(request):
    student = User.objects.filter(is_active=True,is_staff=False,is_superuser=False)
    data = teacher_detailes.objects.get(user__id=request.user.id)
    return render(request,'teacher_panel/student_list.html',{'student':student,"data":data})

@login_required
def add_photo(request):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data
    if request.method == "POST":
        title = request.POST['title']
        itype = request.POST['itype']
        desc = request.POST['desc']

        content = add_photos.objects.create()
        content.title = title
        content.catagory = itype
        content.description = desc
        content.save()

        if 'file' in request.FILES:
            img = request.FILES["file"]
            content.photo = img
            content.save()
        context["status"] = "You Added a Photo Successfully"
    return render(request,'teacher_panel/add_photo.html',context)


@login_required
def posted_photos(request):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data
    photos = add_photos.objects.all().order_by("-id")[:30]
    context['photos'] = photos
    return render(request,'teacher_panel/posted_photo.html',context)

@login_required
def update_photo(request,id):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data
    update = add_photos.objects.get(id=id)
    context['update'] = update

    if request.method == "POST":
        title = request.POST['title']
        itype = request.POST['itype']
        desc = request.POST['desc']
        update.title = title
        update.catagory = itype
        update.description = desc
        update.save()

        if 'file' in request.FILES:
            img = request.FILES["file"]
            update.photo = img
            update.save()
        context['status'] = "You Updated Successfully"
        
    return render(request,'teacher_panel/update_photo.html',context)


@login_required
def delete_photo(request,id):
    context = {}
    delete_item = add_photos.objects.get(id=id)
    delete_item.delete()
    photos = add_photos.objects.all().order_by("-id")[:30]
    context['photos'] = photos
    context['delete_status'] = "You deleted a Photo With Title: {} ".format(delete_item.title)
    return render(request,'teacher_panel/posted_photo.html',context)




@login_required
def add_notifications(request):
    context = {}
    data = teacher_detailes.objects.get(user__id=request.user.id)
    context['data'] = data
    if request.method == "POST":
        title_notification = request.POST['title_notification']
        notification = request.POST['notification']

        notification_content = add_notification.objects.create()
        notification_content.title_notification = title_notification
        notification_content.notification = notification
        notification_content.save()

        if 'file_notification' in request.FILES:
            img = request.FILES["file_notification"]
            notification_content.photo_notification = img
            notification_content.save()
        context["status_notification"] = "You Posted a notification Successfully"
    return render(request,'teacher_panel/add_notification.html',context)


