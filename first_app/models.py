from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList , on_delete=models.CASCADE) #item_set 
    text = models.CharField(max_length=20)
    complete = models.BooleanField()
    def __str__(self):

        return self.text
    