from django.db import models

# Create your models here.


class Student(models.Model):
	student_id = models.CharField(max_length=200)
	student_name = models.CharField(max_length=200)
	branch  = models.CharField(max_length=200)
	college_name = models.CharField(max_length=200)

	def __str__(self):
		return self.student_id + ' ' + self.student_name +' '+ self.branch + ' ' + self.college_name;
	
