from django.contrib import admin
from myapp.models import register_user,contactForm

# Register your models here.
admin.site.site_header = 'COLLEGE CRM'
admin.site.register(register_user)
admin.site.register(contactForm)

