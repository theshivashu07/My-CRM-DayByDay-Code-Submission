from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"dailyTasks/date-20210526/welcome.html")


#---------------------------------------------------------------------------------------


def onlysum1(request):
	return render(request,"dailyTasks/date-20210526/onlysum.html")

def onlysum2(request):
	a=int(request.GET["txtnum1"])
	b=int(request.GET["txtnum2"])
	c=a+b
	return render(request,"dailyTasks/date-20210526/onlysum.html",{'result':c})


#---------------------------------------------------------------------------------------


def checkprime1(request):
	return render(request,"dailyTasks/date-20210526/checkprime.html")

def checkprime2(request):
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


def middleno1(request):
	return render(request,"dailyTasks/date-20210526/middleno.html")

def middleno2(request):
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


def largestno1(request):
	return render(request,"dailyTasks/date-20210526/largestno.html")

def largestno2(request):
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


def markseetstudent1(request):
	return render(request,"dailyTasks/date-20210526/markseetstudent.html")

def markseetstudent2(request):
	m1,m2,m3,m4,m5=int(request.GET["txtnum12"]),int(request.GET["txtnum22"]),int(request.GET["txtnum32"]),int(request.GET["txtnum42"]),int(request.GET["txtnum52"]);
	s1,s2,s3,s4,s5 = request.GET["txtnum11"],request.GET["txtnum21"],request.GET["txtnum31"],request.GET["txtnum41"],request.GET["txtnum51"];
	x=mark=0; sub=dist=''; result=[];
	if((m1>=0 and m1<=100) and (m2>=0 and m2<=100) and (m3>=0 and m3<=100) and (m4>=0 and m4<=100) and (m5>=0 and m5<=100)):     #1
		if(m1<33 or m1>=75):     #2
			if(m1<33):      #3
				x=x+1; mark=m1; sub=sub+s1 +" ";       #4
			else:     #3
				dist=dist+s1+ " ";       #4
		if(m2<33 or m2>=75):    #2
			if(m2<33):      #3
				x=x+1; mark=m2; sub += s2 + " ";       #4
			else:     #3
				dist= dist+s2 + " ";       #4
		if(m3<33 or m3>=75):    #2
			if(m3<33):      #3
				x=x+1; mark=m3; sub=sub+s3 +" ";       #4
			else:   #3
				dist= dist+s3 +" ";       #4
		if(m4<33 or m4>=75):    #2
			if(m4<33):      #3
				x=x+1; mark=m4; sub=sub+s4 +" ";       #4
			else:     #3
				dist= dist+s4 +" ";       #4
		if(m5<33 or m5>=75):    #2
			if(m5<33):      #3
				x=x+1; mark=m5; sub= sub + s5 + " ";       #4
			else:     #3
				dist= dist+s5 +" ";       #4
		if((x==0) or (x==1 and mark>=28)):       #2
			if(x==0):       #3
				per = (m1+m2+m3+m4+m5)/5;       #4
			else:       #3
				per = (m1+m2+m3+m4+m5+(33-mark))/5       #4
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

