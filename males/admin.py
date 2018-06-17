from django.contrib import admin

# Register your models here
from .models import Male

class MaleModelAdmin(admin.ModelAdmin):
    list_display = ["image"]
    class Meta:
        model = Male

admin.site.register(Male, MaleModelAdmin)