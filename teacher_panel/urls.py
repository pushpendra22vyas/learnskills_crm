from os import name
from django.urls import path
from teacher_panel import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'teacher_panel'

urlpatterns = [
    path('',views.teacher_dashboard,name='teacher_dashboard'),
    path('teacher_logout/',views.teacher_logout,name='teacher_logout'),
    path('edit_teacher_profile',views.edit_teacher_profile,name='edit_teacher_profile'),
    path('change_teacher_password/',views.change_teacher_password,name='change_teacher_password'),
    path('delete_teacher_profile/',views.delete_teacher_profile,name='delete_teacher_profile'),
    path('confirm_teacher_delete',views.confirm_teacher_delete,name='confirm_teacher_delete'),
    path('student_list/',views.student_list,name='student_list'),
    path('add_notification/',views.add_notifications,name='add_notification'),
    path('add_photo/',views.add_photo,name='add_photo'),
    path('posted_photos/',views.posted_photos,name='posted_photos'),
    path('update_photo/<int:id>',views.update_photo,name='update_photo'),
    path('delete_item/<int:id>',views.delete_photo,name='delete_photo'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
