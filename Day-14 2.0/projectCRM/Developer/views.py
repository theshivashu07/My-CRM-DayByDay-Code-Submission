from django.shortcuts import render
from django.http import HttpResponse
from dailyTasks.models import Registration


def login(request):
	if request.method=="POST":
		UserNameorEmail=request.POST["txtunameoremail"]
		password=request.POST["txtpass"]
		value=Registration.objects.all()
		for data in value:
			if((data.userName==UserNameorEmail or data.emailId==UserNameorEmail) and (data.password==password)):
				msg="Your UserName/EmailId and Password is Correct";
				break;
		else:
			msg="Your UserName/EmailId and Password is Incorrect";
		return render(request,"Developer/logins.html",{"result":msg});
	return render(request,"Developer/logins.html");

def signup(request):
	if request.method=="POST":
		values=Registration(userName=request.POST["txtuname"],emailId=request.POST["txtemail"],password=request.POST["txtpass"],fullName=request.POST["txtfname"],Age=request.POST["txtage"],mobileNumber=request.POST["txtmobile"])
		values.save()
		return render(request,"Developer/signup.html",{"result":"Registration Successfully"})
	return render(request,"Developer/signup.html");

