from django.contrib import admin
from .models import CustomUser

class CustomAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(CustomUser, CustomAdmin)