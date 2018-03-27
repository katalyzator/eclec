from django.contrib import admin

from .models import *


# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    fields = ('time', 'email', 'phone', 'address', 'location')
    list_display = ('title',)


admin.site.register(AboutUS)
admin.site.register(Contacts, ContactsAdmin)
