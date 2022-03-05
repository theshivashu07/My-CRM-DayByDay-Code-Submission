from django.shortcuts import render
from django.http import HttpResponse
from django.views import View





#---------------------------------------------------------------------------------------
class assignment1(View):
	def post(self,request):
		selection = request.POST["selection"]
		p1=float(request.POST["txtnum1"])
		p2=float(request.POST["txtnum2"])
		if(selection=="triangle"):
			result=["Height is "+str(p1),"Base is "+str(p2),"Area of triangle is : "+str((1/2)*p1*p2)]
		elif(selection=="rectangle"):
			result=["Height is "+str(p1),"Width is "+str(p2),"Area of rectangle is : "+str(p1*p2)]
		return render(request,"dailyTasks/date-20210608for03/assignment1.html",{'value':result,"choice":selection,"txtbox1":request.POST["txtnum1"],"txtbox2":request.POST["txtnum2"]})
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/assignment1.html")

#---------------------------------------------------------------------------------------
class assignment2(View):
	def post(self,request):
		selection = request.POST["selection"]
		return render(request,"dailyTasks/date-20210608for03/assignment2.html",{'result':selection})
	def get(self,request):
		selection="None";
		return render(request,"dailyTasks/date-20210608for03/assignment2.html",{'result':selection})

#---------------------------------------------------------------------------------------
class assignment2sep(View):
	def post(self,request):
		selection = request.POST["selection"]
		return render(request,"dailyTasks/date-20210608for03/assignment2(saperatepage).html",{'result':selection})
	def get(self,request):
		selection="";
		return render(request,"dailyTasks/date-20210608for03/assignment2(saperatepage).html",{'result':selection})

#---------------------------------------------------------------------------------------
class assignment3(View):
	def post(self,request):
		courses = request.POST.getlist("course[]")
		selection = request.POST["selection"]
		lst=[]; fee=0; valueC=""; k=len(courses)
		for initial in courses:
			valueC = valueC+initial if(k==1) else valueC+initial+", ";
			k-=1;
			if(initial=="C"):
				fee+=2000;
			elif(initial=="CPP"):
				fee+=3000;
			elif(initial=="DS"):
				fee+=3500;
		lst+=["Basic Courses : "+valueC]
		if(selection==".NET"):
			fee+=8000;
		elif(selection=="PHP"):
			fee+=10000;
		elif(selection=="JAVA"):
			fee+=10000;
		elif(selection=="PYTHON"):
			fee+=12000;
		lst+=["Advanced Courses : "+selection]
		lst+=["Overall Fee is : "+str(fee)]
		return render(request,"dailyTasks/date-20210608for03/assignment3.html",{'data':lst,'val':k,'select':courses,'choice':selection})
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/assignment3.html")

#---------------------------------------------------------------------------------------
class assignment4(View):
	def post(self,request):
		Country = request.POST["CountryName"]
		Cities=[Country+"'s Cities :"]
		if(Country=='America'):
			Cities+=["New York","Atlanta","Washington DC","Chicago","Austin"]
		elif(Country=='Australia'):
			Cities+=["Sydney","Melbourne","Brisbane","Perth","Adelaide"]
		elif(Country=='China'):
			Cities+=["Shanghai","Beijing","Tianjin","Shenzhen","Guangzhou"]
		elif(Country=='India'):
			Cities+=["Mumbai","Delhi","Bangalore","Chennai","Pune"]
		elif(Country=='Russia'):
			Cities+=["Moscow","St. Petersburg","Novosibirsk","Yekaterinburg","Kazan"]
		return render(request,"dailyTasks/date-20210608for03/assignment4.html",{'data':Cities,'choice':Country})
	def get(self,request):
		Cities=["empty"];
		return render(request,"dailyTasks/date-20210608for03/assignment4.html",{'data':Cities})

#---------------------------------------------------------------------------------------
class feedback(View):
	def post(self,request):
		name = request.POST["txtname"]
		gender = request.POST["gender"]
		courses = request.POST.getlist("course[]")
		branches = request.POST.getlist("branch[]")
		feeds = request.POST["feed"]
		cource=branch="";
		for data in courses:
			cource=cource+data+" ";
		for data in branches:
			branch=branch+data+" ";
		result = ["Hey " + name,"Your Gender is " + gender, "Your selected courses is " + cource,"and Branchs is "+ branch,"and feedback is " + feeds]
		return render(request,"dailyTasks/date-20210608for03/feedback.html",{"data":result,"txtbox1":name,"choice":gender,"select":courses,"feedchoice":feeds,"branch":branches})  
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/feedback.html")

#---------------------------------------------------------------------------------------
class onlysum(View):
	def post(self,request):
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=a+b
		return render(request,"dailyTasks/date-20210608for03/onlysum.html",{'result':c,'txtbox1':request.POST["txtnum1"],'txtbox2':request.POST["txtnum2"]})
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/onlysum.html")

#---------------------------------------------------------------------------------------
class checkprime(View):
	def post(self,request):
		val=int(request.POST["txtnum1"])
		if(val>1):
			for num in range(2,val):
				if(val%num==0):
					s="It's not a primeNumber, and devided by "+str(num);
					break;
			else:
				s="It's a primeNumber";
		return render(request,"dailyTasks/date-20210608for03/checkprime.html",{'result':s,'txtbox1':request.POST["txtnum1"]});
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/checkprime.html");

#---------------------------------------------------------------------------------------
class factorial(View):
	def post(self,request):
		value=int(request.POST["txtnum1"])
		calc=1
		for i in range(1,value+1):
			calc*=i;
		return render(request,"dailyTasks/date-20210608for03/factorial.html",{'result':calc,'txtbox1':request.POST["txtnum1"]})
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/factorial.html")

#---------------------------------------------------------------------------------------
class middleno(View):
	def post(self,request):
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=int(request.POST["txtnum3"])
		if((a>b and a<c) or (a>c and a<b)):
			k=a
		elif((b>a and b<c) or (b>c and b<a)):
			k=b
		else:
			k=c
		return render(request,"dailyTasks/date-20210608for03/middleno.html",{'result':k,'txtbox1':request.POST["txtnum1"],'txtbox2':request.POST["txtnum2"],'txtbox3':request.POST["txtnum3"]})
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/middleno.html")

#---------------------------------------------------------------------------------------
class largestno(View):
	def post(self,request):
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=int(request.POST["txtnum3"])
		if(a>b):
			if(a>c):
				k=a;
			else:
				k=c;
		else:
			if(b>c):
				k=b;
			else:
				k=c;
		return render(request,"dailyTasks/date-20210608for03/largestno.html",{'result':k,'txtbox1':request.POST["txtnum1"],'txtbox2':request.POST["txtnum2"],'txtbox3':request.POST["txtnum3"]})
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/largestno.html")

#---------------------------------------------------------------------------------------
class markseetstudent(View):
	def post(self,request):
		data= {request.POST["txtnum11"]:int(request.POST["txtnum12"]),request.POST["txtnum21"]:int(request.POST["txtnum22"]),request.POST["txtnum31"]:int(request.POST["txtnum32"]),request.POST["txtnum41"]:int(request.POST["txtnum42"]),request.POST["txtnum51"]:int(request.POST["txtnum52"])};
		marks=list(data.values()); 	subj= list(data.keys());
		x=mark=0; sub=dist=''; result=[];
		if((marks[0]>=0 and marks[0]<=100) and (marks[1]>=0 and marks[1]<=100) and (marks[2]>=0 and marks[2]<=100) and (marks[3]>=0 and marks[3]<=100) and (marks[4]>=0 and marks[4]<=100)):     #1
			for i in range(0,5):
				if(marks[i]<33 or marks[i]>=75):     #3
					if(marks[i]<33):      #4
						x=x+1; mark=marks[i]; sub += subj[i] +" ";       #5
					else:     #4
						dist= dist+ subj[i] +" ";       #5
			if((x==0) or (x==1 and mark>=28)):       #2
				if(x==0):       #3
					per = (marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/5;       #4
				else:       #3
					per = (marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+(33-mark))/5       #4
				if(per>=33 and per<45):       #3
					result.append("Pass with Third division "+str(per) + "%")       #4
				elif(per>=45 and per<60):       #3
					result.append("Pass with Second division "+str(per) + "%")       #4
				else:       #3
					result.append("Pass with First Division "+str(per) + "%")       #4
				if(x==1):       #3
					result.append("You are pass by grace and grace mark is "+str(33-mark) + ", subject is "+sub)       #4
				if(not(dist=="")):       #3
					result.append("Distinction subject name are "+dist)       #4
			elif(x==1):       #2
				result.append("suppl in "+sub);       #3
			else:       #2
				result.append("failed in "+sub);       #3
		else:       #1
			result.append("invalid marks");       #2
		return render(request,"dailyTasks/date-20210608for03/markseetstudent.html",{'result':result,'txtbox11':request.POST["txtnum11"],'txtbox12':request.POST["txtnum12"],'txtbox21':request.POST["txtnum21"],'txtbox22':request.POST["txtnum22"],'txtbox31':request.POST["txtnum31"],'txtbox32':request.POST["txtnum32"],'txtbox41':request.POST["txtnum41"],'txtbox42':request.POST["txtnum42"],'txtbox51':request.POST["txtnum51"],'txtbox52':request.POST["txtnum52"]})
	def get(self,request):
		return render(request,"dailyTasks/date-20210608for03/markseetstudent.html")




#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

