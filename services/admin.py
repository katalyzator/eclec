from django.contrib import admin

from .models import *


# Register your models here.
class ApplicatonAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'phone', 'date')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'category')


admin.site.register(Category)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Application, ApplicatonAdmin)
