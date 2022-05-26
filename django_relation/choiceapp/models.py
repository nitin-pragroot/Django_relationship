from django.db import models


# Specifying Choices

Semester_choices = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
   
)

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    age = models.IntegerField()
    course = models.CharField(max_length=20,null=True,blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    semester = models.CharField(max_length=30,
                choices = Semester_choices , default = 1)
    
    def __str__(self):
        return self.name
    
