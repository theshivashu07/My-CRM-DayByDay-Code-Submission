from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration

def index(request):
	return render(request,"dailyTasks/welcome.html")

def showRegistrations20210611(request):
	value=Registration.objects.all()	#select *from Registration
	return render(request,"dailyTasks/date-20210611/showRegistrations.html",{"result":value})

