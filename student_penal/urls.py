from django.urls import path
from student_penal import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'student_panel'

urlpatterns = [
    path('',views.student_dashboard,name='stud_dash'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('delete_profile/',views.delete_profile,name='delete_profile'),
    path('confirm_delete/',views.confirm_delete,name='confirm_delete'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
