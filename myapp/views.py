from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from myapp.models import contactForm, register_user
from teacher_panel.models import add_notification
from teacher_panel.models import teacher_detailes,add_photos
from django.contrib.auth import login, authenticate


# Create your views here.
def Index(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        notification = add_notification.objects.all().order_by("-id")[:8]
        hostel_index = add_photos.objects.filter(catagory="Hostel").order_by("?")[:1]
        library_index = add_photos.objects.filter(catagory="Library").order_by("-id")[:1]
        context['notification'] = notification
        context['hostel_index'] = hostel_index
        context['library_index'] = library_index
        return render(request,'myapp/index.html',context)
    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        notification = add_notification.objects.all().order_by("-id")[:8]
        hostel_index = add_photos.objects.filter(catagory="Hostel").order_by("?")[:1]
        library_index = add_photos.objects.filter(catagory="Library").order_by("-id")[:1]
        context['notification'] = notification
        context['hostel_index'] = hostel_index
        context['library_index'] = library_index
        return render(request,'myapp/index.html',context)

    else:
        context = {}
        notification = add_notification.objects.all().order_by("-id")[:8]
        hostel_index = add_photos.objects.filter(catagory="Hostel").order_by("?")[:1]
        library_index = add_photos.objects.filter(catagory="Library").order_by("-id")[:1]
        context['notification'] = notification
        context['hostel_index'] = hostel_index
        context['library_index'] = library_index
        return render(request,'myapp/index.html',context)


def User_Registration(request):
    if request.method =='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['password']
        email = request.POST['email']
        utype = request.POST['utype']

        
        usr = User.objects.create_user(uname,email,password)
        usr.first_name = fname
        usr.last_name = lname
        

        if utype == 'teacher':
            usr.is_staff = True
        usr.save()

      
        
        if utype == 'teacher':
            reg = teacher_detailes(user=usr)
            reg.save()
        else:
            regs = register_user(user=usr)
            regs.save()

        return render(request,'myapp/index.html',{"status":"You Registered With {} as a  {} ".format(fname,utype)})

    
    return render(request,'myapp/registration.html')




def check_username(request):
    if request.method == "GET":
        un = request.GET['user_name']
        check = User.objects.filter(username=un)

        if len(check) == 1:
            return HttpResponse('Exisits')
        else:   
            return HttpResponse('not Exisits')






def user_login(request):
    if request.method =="POST":
        un = request.POST['username']
        pw = request.POST["password"]

        user = authenticate(username=un,password=pw)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            if user.is_staff:
                return HttpResponseRedirect("/teacher_panel")
            if user.is_active:
                return HttpResponseRedirect("/student_panel")
        else:
            return render(request,"myapp/index.html",{"valid":"Invalid Username or Password"})


def ug_program(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/navbar/addmission/ug_program.html',context)
    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/navbar/addmission/ug_program.html',context)

    else:
        return render(request,'myapp/navbar/addmission/ug_program.html')

def pg_program(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/navbar/addmission/pg_program.html',context)

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/navbar/addmission/pg_program.html',context)
    else:
        return render(request,'myapp/navbar/addmission/pg_program.html')

def doctoral_program(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/navbar/addmission/doctoral_program.html',context)

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/navbar/addmission/doctoral_program.html',context)
    else:
        return render(request,'myapp/navbar/addmission/doctoral_program.html')


def principal(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/administration/principal.html',context)
        
    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/administration/principal.html',context)
    else:
        return render(request,'myapp/administration/principal.html')

def teacher(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        teacher = User.objects.filter(is_staff=True,is_superuser=False)
        return render(request,'myapp/administration/staff.html',{'teacher':teacher,'data':data})

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        teacher = User.objects.filter(is_staff=True,is_superuser=False)
        return render(request,'myapp/administration/staff.html',{'teacher':teacher,'data':data})
    else:
        teacher = User.objects.filter(is_staff=True,is_superuser=False)
        return render(request,'myapp/administration/staff.html',{'teacher':teacher})

def hostels(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/campus_life/hostel.html',context)

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/campus_life/hostel.html',context)
    else:
        return render(request,'myapp/campus_life/hostel.html')

def library(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/campus_life/library.html',context)

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/campus_life/library.html',context)
    else:
        return render(request,'myapp/campus_life/library.html')
    

def canteen_guesthouse(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/campus_life/canteen_guesthouse.html',context)

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request,'myapp/campus_life/canteen_guesthouse.html',context)
    else:
        return render(request,'myapp/campus_life/canteen_guesthouse.html')

def sports(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request, 'myapp/campus_life/sports.html',context)

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        return render(request, 'myapp/campus_life/sports.html',context)
    else:
        return render(request, 'myapp/campus_life/sports.html')


def contect_us(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mn = request.POST['mn']
        message = request.POST['message']

        contact = contactForm.objects.create()
        contact.fname = fname
        contact.lname = lname
        contact.email = email
        contact.mn = mn 
        contact.message = message

        contact.save()
        return render(request,'myapp/index.html' ,{"contact_status":"Your Message Successfully Sent"})

    return render(request,'myapp/contect_us.html')

def gallery(request):
    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        context['range'] = range(1,10)
        hostel = add_photos.objects.filter(catagory="Hostel").order_by("-id")[:30]
        library = add_photos.objects.filter(catagory="Library").order_by("-id")[:30]
        sports = add_photos.objects.filter(catagory="Sports").order_by("-id")[:30]
        canteen = add_photos.objects.filter(catagory="Canteen").order_by("-id")[:30]


        # HOSTEL SECTION
        ph = Paginator(hostel,4)
        page_number = request.GET.get('page')
        hostel = ph.get_page(page_number)
        context['hostel'] = hostel

        # LIBRARY SECTION
        pl = Paginator(library,4)
        page_number = request.GET.get('page')
        library = pl.get_page(page_number)
        context['library'] = library

        # SPORTS SECTION
        ps = Paginator(sports,4)
        page_number = request.GET.get('page')
        sports = ps.get_page(page_number)
        context['sports'] = sports
        
        # CANTEEN SECTION
        pc = Paginator(canteen,4)
        page_number = request.GET.get('page')
        canteen = pc.get_page(page_number)
        context['canteen'] = canteen
        return render(request,'myapp/gallery.html',context)

    elif request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        context['range'] = range(1,10)
        hostel = add_photos.objects.filter(catagory="Hostel").order_by("-id")[:30]
        library = add_photos.objects.filter(catagory="Library").order_by("-id")[:30]
        sports = add_photos.objects.filter(catagory="Sports").order_by("-id")[:30]
        canteen = add_photos.objects.filter(catagory="Canteen").order_by("-id")[:30]


        # HOSTEL SECTION
        ph = Paginator(hostel,4)
        page_number = request.GET.get('page')
        hostel = ph.get_page(page_number)
        context['hostel'] = hostel

        # LIBRARY SECTION
        pl = Paginator(library,4)
        page_number = request.GET.get('page')
        library = pl.get_page(page_number)
        context['library'] = library

        # SPORTS SECTION
        ps = Paginator(sports,4)
        page_number = request.GET.get('page')
        sports = ps.get_page(page_number)
        context['sports'] = sports
        
        # CANTEEN SECTION
        pc = Paginator(canteen,4)
        page_number = request.GET.get('page')
        canteen = pc.get_page(page_number)
        context['canteen'] = canteen
        return render(request,'myapp/gallery.html',context)

    else:
        context = {}
        context['range'] = range(1,10)
        hostel = add_photos.objects.filter(catagory="Hostel").order_by("-id")[:30]
        library = add_photos.objects.filter(catagory="Library").order_by("-id")[:30]
        sports = add_photos.objects.filter(catagory="Sports").order_by("-id")[:30]
        canteen = add_photos.objects.filter(catagory="Canteen").order_by("-id")[:30]


        # HOSTEL SECTION
        ph = Paginator(hostel,4)
        page_number = request.GET.get('page')
        hostel = ph.get_page(page_number)
        context['hostel'] = hostel

        # LIBRARY SECTION
        pl = Paginator(library,4)
        page_number = request.GET.get('page')
        library = pl.get_page(page_number)
        context['library'] = library

        # SPORTS SECTION
        ps = Paginator(sports,4)
        page_number = request.GET.get('page')
        sports = ps.get_page(page_number)
        context['sports'] = sports
        
        # CANTEEN SECTION
        pc = Paginator(canteen,4)
        page_number = request.GET.get('page')
        canteen = pc.get_page(page_number)
        context['canteen'] = canteen
        return render(request,'myapp/gallery.html',context)


def notifcations_page(request):

    if request.user.is_staff:
        context = {}
        data = teacher_detailes.objects.get(user__id=request.user.id)
        context['data'] = data
        all_notification = add_notification.objects.all().order_by("-id")
        context['all_notification'] = all_notification
        return render(request,'myapp/notifications.html',context)

    if request.user.is_active:
        context = {}
        data = register_user.objects.get(user__id=request.user.id)
        context['data'] = data
        all_notification = add_notification.objects.all().order_by("-id")
        context['all_notification'] = all_notification
        return render(request,'myapp/notifications.html',context)
    else:
        context = {}
        all_notification = add_notification.objects.all().order_by("-id")
        context['all_notification'] = all_notification
        return render(request,'myapp/notifications.html',context)
        
