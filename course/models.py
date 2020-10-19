from django.db import models

# Create your models here.
class Course(models.Model):
	name=models.CharField(max_length=200)
	language=models.CharField(max_length=100)
	price=models.CharField(max_length=20)

# def below changes the display list from “course object (1)” to the actual course name.
	def __str__(self):
		return self.name