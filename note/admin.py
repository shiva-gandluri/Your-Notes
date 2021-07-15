from django.contrib import admin

# Register your models here.
from .models import Note                         #db’s we created

admin.site.register(Note)  