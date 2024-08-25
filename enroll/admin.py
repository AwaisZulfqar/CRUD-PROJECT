from django.contrib import admin
from .models import Registration
# Register your models here.

@admin.register(Registration)
class RegistartionAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')


