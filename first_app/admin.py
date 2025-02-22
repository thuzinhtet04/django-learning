from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)

# run command "python manage.py createsuperuser" to create admin acc
