from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from myapp.models import register_user
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def student_dashboard(request):
    context = {}
    data = register_user.objects.get(user__id=request.user.id)
    context['data'] = data
    return render(request,'student_panel/dashboard.html',context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required
def view_profile(request):
    context = {}
    data = register_user.objects.get(user__id=request.user.id)
    context['data'] = data
    return render(request,'student_panel/view_profile.html',context)


@login_required
def edit_profile(request):
    context = {}
    data = register_user.objects.get(user__id=request.user.id)
    context['data'] = data
    if request.method == "POST":
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        age = request.POST['age']
        branch = request.POST['branch']
        dob = request.POST['dob']
        city = request.POST['city']
        gender = request.POST['gender']
        cn = request.POST['cn']
        sports = request.POST['sports']
        culture = request.POST['cultural']

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()


        data.branch = branch
        data.age = age
        data.dob = dob
        data.city = city
        data.contect_number = cn
        data.gender = gender
        data.sports_activity = sports
        data.culture_activity = culture
        data.save()

        if 'image' in request.FILES:
            img = request.FILES["image"]
            data.profile = img
            data.save()

        
    context['status'] = "You Update Your Profile Successfully"
    return render(request,'student_panel/edit_profile.html',context)

@login_required
def change_password(request):
    context = {}
    data = register_user.objects.get(user__id=request.user.id)
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
    return render(request, 'student_panel/change_password.html',context)

@login_required
def delete_profile(request):
    context = {}
    data = register_user.objects.get(user__id=request.user.id)
    context['data'] = data
    return render(request,'student_panel/delete_profile.html',context)


@login_required
def confirm_delete(request):
    user = User.objects.get(id = request.user.id)
    user.delete()
    return redirect("/")