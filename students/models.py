from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
