from django.contrib import admin
from teacher_panel.models import teacher_detailes, add_photos,add_notification

# Register your models here.
admin.site.register(teacher_detailes)
admin.site.register(add_photos)
admin.site.register(add_notification)
