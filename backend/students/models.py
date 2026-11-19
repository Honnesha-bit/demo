from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    department=models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
#  these are the orm operation 
# retrive the student by Name
# rtrive only email
# count total students
# update student's age

