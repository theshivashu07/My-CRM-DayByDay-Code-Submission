from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration,Course,Student


def index(request):
	if request.method=="POST":
		UserNameorEmail=request.POST["txtunameoremail"]
		password=request.POST["txtpass"]
		value=Registration.objects.all()
		for data in value:
			if((data.userName==UserNameorEmail or data.emailId==UserNameorEmail) and (data.password==password)):
				return render(request,"dailyTasks/welcome.html");
		else:
			msg="Your UserName/EmailId and Password is Incorrect";
			return render(request,"dailyTasks/date-20210617/login.html",{"result":msg});
	return render(request,"dailyTasks/date-20210617/login.html")

def showRegistrations20210611(request):
	value=Registration.objects.all()	#select *from Registration
	return render(request,"dailyTasks/date-20210611/showRegistrations.html",{"result":value})





def addCourse20210615(request):
	if request.method=="POST":
		values=Course(branch=request.POST["txtnum1"],courseIdC=request.POST["txtnum2"],courceName=request.POST["txtnum3"],courseFee=request.POST["txtnum4"])
		values.save()
		return render(request,"dailyTasks/date-20210615/addCourse.html",{"result":"Course's Record Successfully Added"})
	return render(request,"dailyTasks/date-20210615/addCourse.html")

def viewCourse20210615(request):
	value=list(Course.objects.all());	#select *from Course
	return render(request,"dailyTasks/date-20210615/viewCourse.html",{"result":value})

def addStudent20210615(request):
	if request.method=="POST":
		values=Student(rollNo=request.POST["txtnum1"],studentName=request.POST["txtnum2"],courseIdS=request.POST["cId"])
		values.save()
		return render(request,"dailyTasks/date-20210615/addStudent.html",{"result":"Student's Record Successfully Added"})
	value=Course.objects.all()	#select *from Registration
	return render(request,"dailyTasks/date-20210615/addStudent.html",{"courses":value})





def tryFunc():
	valueC=Course.objects.all();	#select *from Course
	valueS=Student.objects.all();	#select *from Student
	value=[]
	for k in range(0,len(valueS)):
		have=[]
		having=valueS[k].courseIdS;
		for l in range(0,len(valueC)):
			if(having==valueC[l].courseIdC):
				have.append(valueS[k]);
				have.append(valueC[l]);
				break;
		value.append(have);
	result=[];
	for k in range(0,len(value)):
		result.append({"branch":value[k][1].branch,"courseIdS":value[k][0].courseIdS,"courceName":value[k][1].courceName,"rollNo":value[k][0].rollNo,"studentName":value[k][0].studentName,"courseFee":value[k][1].courseFee})
	return result;

def viewStudent20210615(request):
	result=tryFunc();
	return render(request,"dailyTasks/date-20210615/viewStudent.html",{"result":result})


