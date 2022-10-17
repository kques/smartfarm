from django.contrib import admin
from .models import Aduino

class AduinoAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Aduino, AduinoAdmin)