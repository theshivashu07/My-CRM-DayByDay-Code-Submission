from django.db import models

class Registration(models.Model):
	userName = models.CharField(max_length=15)
	emailId = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	fullName = models.CharField(max_length=25)
	Age = models.CharField(max_length=2)
	mobileNumber = models.CharField(max_length=10)
	def __str__(self):
		return self.fullName+", as "+self.userName;


class Course(models.Model): 
	branch = models.CharField(max_length=10)
	courseIdC = models.CharField(max_length=10)
	courceName = models.CharField(max_length=30)
	courseFee = models.CharField(max_length=5)
	def __str__(self):
		return self.courseIdC+" : "+self.courceName;


class Student(models.Model): 
	rollNo = models.CharField(max_length=10)
	studentName = models.CharField(max_length=30)
	courseIdS = models.CharField(max_length=15)
	def __str__(self):
		return self.rollNo+" : "+self.studentName; 

