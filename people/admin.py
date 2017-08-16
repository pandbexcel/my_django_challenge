from django.contrib import admin

# Register your models here.
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','nickname','email']

admin.site.register(Person, PersonAdmin)