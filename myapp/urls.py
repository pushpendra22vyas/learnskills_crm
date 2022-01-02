from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [
    path('',views.Index,name='index'),
    path('registration/',views.User_Registration,name='registration'),
    path('check_username/',views.check_username,name='check_username'),
    path('user_login/',views.user_login,name="user_login"),
    path('ug_program/',views.ug_program,name='ug_program'),
    path('pg_program/',views.pg_program,name='pg_program'),
    path('doctoral_program/',views.doctoral_program,name='doctoral_program'),
    path('principal/',views.principal,name='principal'),
    path('teacher/',views.teacher,name='teacher'),
    path('hostel/',views.hostels,name='hostel'),
    path('library/',views.library,name='library'),
    path('canteen_guest_house/',views.canteen_guesthouse,name='canteen_guest_house'),
    path('sports/',views.sports,name='sports'),
    path('contect_us/',views.contect_us,name='contect_us'),
    path('gallery/',views.gallery,name='gallery'),
    path('notifications/',views.notifcations_page,name='notifications_page'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
