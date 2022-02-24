from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"dailyTasks/welcome.html")


#---------------------------------------------------------------------------------------


def onlysum202105261(request):
	return render(request,"dailyTasks/date-20210526/onlysum.html")

def onlysum202105262(request):
	a=int(request.GET["txtnum1"])
	b=int(request.GET["txtnum2"])
	c=a+b
	return render(request,"dailyTasks/date-20210526/onlysum.html",{'result':c})


#---------------------------------------------------------------------------------------


def checkprime202105261(request):
	return render(request,"dailyTasks/date-20210526/checkprime.html")

def checkprime202105262(request):
	val=int(request.GET["txtnum1"])
	if(val>1):
		for num in range(2,val):
			if(val%num==0):
				s="It's not a primeNumber, and devided by "+str(num);
				break;
		else:
			s="It's a primeNumber"
	return render(request,"dailyTasks/date-20210526/checkprime.html",{'result':s})


#---------------------------------------------------------------------------------------


def factorial202105261(request):
	return render(request,"dailyTasks/date-20210526/factorial.html")

def factorial202105262(request):
	value=int(request.GET["txtnum1"])
	calc=1
	for i in range(1,value+1):
		calc*=i;
	return render(request,"dailyTasks/date-20210526/factorial.html",{'result':calc})


#---------------------------------------------------------------------------------------


def middleno202105261(request):
	return render(request,"dailyTasks/date-20210526/middleno.html")

def middleno202105262(request):
	a=int(request.GET["txtnum1"])
	b=int(request.GET["txtnum2"])
	c=int(request.GET["txtnum3"])
	if((a>b and a<c) or (a>c and a<b)):
		k=a
	elif((b>a and b<c) or (b>c and b<a)):
		k=b
	else:
		k=c
	return render(request,"dailyTasks/date-20210526/middleno.html",{'result':k})


#---------------------------------------------------------------------------------------


def largestno202105261(request):
	return render(request,"dailyTasks/date-20210526/largestno.html")

def largestno202105262(request):
	a=int(request.GET["txtnum1"])
	b=int(request.GET["txtnum2"])
	c=int(request.GET["txtnum3"])
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
	return render(request,"dailyTasks/date-20210526/largestno.html",{'result':k})


#---------------------------------------------------------------------------------------


def markseetstudent202105261(request):
	return render(request,"dailyTasks/date-20210526/markseetstudent.html")

def markseetstudent202105262(request):
	data= {request.GET["txtnum11"]:int(request.GET["txtnum12"]),request.GET["txtnum21"]:int(request.GET["txtnum22"]),request.GET["txtnum31"]:int(request.GET["txtnum32"]),request.GET["txtnum41"]:int(request.GET["txtnum42"]),request.GET["txtnum51"]:int(request.GET["txtnum52"])};
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
	return render(request,"dailyTasks/date-20210526/markseetstudent.html",{'result':result})


#---------------------------------------------------------------------------------------

'''
def markseetstudent202105261(request):
	return render(request,"dailyTasks/date-20210526/markseetstudent.html")

def markseetstudent202105262(request):
	marks= [int(request.GET["txtnum12"]),int(request.GET["txtnum22"]),int(request.GET["txtnum32"]),int(request.GET["txtnum42"]),int(request.GET["txtnum52"])];
	subj = [request.GET["txtnum11"],request.GET["txtnum21"],request.GET["txtnum31"],request.GET["txtnum41"],request.GET["txtnum51"]];
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
	return render(request,"dailyTasks/date-20210526/markseetstudent.html",{'result':result})
'''




#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------





def onlysum202105271(request):
	return render(request,"dailyTasks/date-20210527/onlysum.html")

def onlysum202105272(request):
	a=int(request.POST["txtnum1"])
	b=int(request.POST["txtnum2"])
	c=a+b
	return render(request,"dailyTasks/date-20210527/onlysum.html",{'result':c})


#---------------------------------------------------------------------------------------


def checkprime202105271(request):
	return render(request,"dailyTasks/date-20210527/checkprime.html")

def checkprime202105272(request):
	val=int(request.POST["txtnum1"])
	if(val>1):
		for num in range(2,val):
			if(val%num==0):
				s="It's not a primeNumber, and devided by "+str(num);
				break;
		else:
			s="It's a primeNumber"
	return render(request,"dailyTasks/date-20210527/checkprime.html",{'result':s})


#---------------------------------------------------------------------------------------


def factorial202105271(request):
	return render(request,"dailyTasks/date-20210527/factorial.html")

def factorial202105272(request):
	value=int(request.POST["txtnum1"])
	calc=1
	for i in range(1,value+1):
		calc*=i;
	return render(request,"dailyTasks/date-20210527/factorial.html",{'result':calc})


#---------------------------------------------------------------------------------------


def middleno202105271(request):
	return render(request,"dailyTasks/date-20210527/middleno.html")

def middleno202105272(request):
	a=int(request.POST["txtnum1"])
	b=int(request.POST["txtnum2"])
	c=int(request.POST["txtnum3"])
	if((a>b and a<c) or (a>c and a<b)):
		k=a
	elif((b>a and b<c) or (b>c and b<a)):
		k=b
	else:
		k=c
	return render(request,"dailyTasks/date-20210527/middleno.html",{'result':k})


#---------------------------------------------------------------------------------------


def largestno202105271(request):
	return render(request,"dailyTasks/date-20210527/largestno.html")

def largestno202105272(request):
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
	return render(request,"dailyTasks/date-20210527/largestno.html",{'result':k})


#---------------------------------------------------------------------------------------


def markseetstudent202105271(request):
	return render(request,"dailyTasks/date-20210527/markseetstudent.html")

def markseetstudent202105272(request):
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
	return render(request,"dailyTasks/date-20210527/markseetstudent.html",{'result':result})





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------





