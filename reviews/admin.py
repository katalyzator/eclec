from django.contrib import admin

from .models import *
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'date')

admin.site.register(Review, ReviewAdmin)