from django.db import models

# Create your models here.
class Student(models.Model):
    Full_Name = models.CharField(max_length=100)
    Mobile =models.IntegerField()
    Email = models.EmailField(max_length=50)
    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),
    )
    Gender = models.CharField(max_length=50, choices=GENDER)
    Student_Number = models.IntegerField(unique=True, null=True, blank=True)
    PATH = (        
        ("1", "Full Stack"),
        ("2", "AWS-DevOps"),
        ("3", "Data Science"),
        ("4", "Cyber Security"),
    )

    Path = models.CharField(max_length=50, choices=PATH) 
    def __str__(self):
        return f"{self.Full_Name} {self.Mobile} {self.Email} {self.Student_Number}"

