from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration

def index(request):
	return render(request,"dailyTasks/welcome.html")

def showRegistrations20210611(request):
	value=Registration.objects.all()	#select *from Registration
	return render(request,"dailyTasks/date-20210611/showRegistrations.html",{"result":value})

def showContentWise20210611(request):
	if request.method=="POST":
		selects = request.POST["selected"];
		txtAnything = request.POST["txtanything"]
		having=[]
		value=Registration.objects.all()	#select *from Registration
		for data in value:
			if(data.str(selects)==txtAnything):
				having.append(data);
		return render(request,"dailyTasks/date-20210611/showContentWise.html",{"result":having})
	return render(request,"dailyTasks/date-20210611/showContentWise.html")


