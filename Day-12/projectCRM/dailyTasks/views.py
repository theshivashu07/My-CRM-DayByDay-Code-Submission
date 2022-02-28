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





def starpattern1202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern1.html")

def starpattern1202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(1,inputs+1):
		hold='  ';
		for j in range(1,inputs+1):
			if(i>=j):
				hold+="* "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern1.html",{'data':lst})



def starpattern2202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern2.html")

def starpattern2202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(1,inputs+1):
		hold='  ';
		for j in range(inputs,0,-1):
			if(i>=j):
				hold+="* "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern2.html",{'data':lst})



def starpattern3202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern3.html")

def starpattern3202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(inputs,0,-1):
		hold='  ';
		for j in range(1,inputs+1):
			if(i>=j):
				hold+="* "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern3.html",{'data':lst})



def starpattern4202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern4.html")

def starpattern4202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(inputs,0,-1):
		hold='  ';
		for j in range(inputs,0,-1):
			if(i>=j):
				hold+="* "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern4.html",{'data':lst})



def starpattern5202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern5.html")

def starpattern5202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(1,inputs+1):
		hold='  ';
		for j in range(1,inputs*2):
			if(inputs-1+i>=j and inputs+1-i<=j):
				hold+="* "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern5.html",{'data':lst})



def starpattern6202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern6.html")

def starpattern6202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(1,inputs+1):
		hold='  ';
		for j in range(1,inputs*2):
			if(inputs-1+i>j and inputs+1-i<j):
				hold+="  "
			else:
				hold+="* "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern6.html",{'data':lst})



def starpattern7202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern7.html")

def starpattern7202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(1,inputs+1):
		k=0
		hold='  ';
		for j in range(1,inputs*2):
			if(inputs-1+i>=j and inputs+1-i<=j):
				k=k+1 if(inputs>=j) else k-1;
				hold+=str(k)+" "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern7.html",{'data':lst})



def starpattern8202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern8.html")

def starpattern8202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(1,inputs+1):
		k=0
		hold='  ';
		for j in range(1,inputs*2):
			k=k+1 if(inputs>=j) else k-1;
			if(inputs-1+i>j and inputs+1-i<j):
				hold+="  "
			else:
				hold+=chr(64+k)+" "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern8.html",{'data':lst})



def starpattern9202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern9.html")

def starpattern9202105282(request):
	inputs=int(request.POST["txtnum1"]);
	lst=[]
	for i in range(1,inputs+1):
		k=0
		hold='  ';
		for j in range(1,inputs*2):
			k=k+1 if(inputs>=j) else k-1;
			if(inputs-1+i>=j and inputs+1-i<=j):
				hold+=str(k)+" "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern9.html",{'data':lst})



def starpattern10202105281(request):
	return render(request,"dailyTasks/date-20210528/starpattern10.html")

def starpattern10202105282(request):
	inputs=int(request.POST["txtnum1"]);
	k=0
	lst=[]
	for i in range(1,inputs*2):
		hold='  ';
		k= k+1 if(inputs>=i) else k-1;
		for j in range(1,inputs*2):
			if(inputs-1+k>=j and inputs+1-k<=j):
				hold+="* "
			else:
				hold+="  "
		lst.append(hold);
	return render(request,"dailyTasks/date-20210528/starpattern10.html",{'data':lst})





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------



def program1202105291(request):
	return render(request,"dailyTasks/date-20210529/program1.html")

def program1202105292(request):
	no=int(request.POST["txtnum1"]);
	i=k=1;
	lst=[]
	no1= 10 if(no%2==1) else no;
	while(i<=no1):
		if(no%2==1):
			lst.append(str(no)+" * "+str(i)+" = "+str(no*i))
		else:
			k=k*i;
			if(i==no1):
				lst.append("factorial of "+str(no)+" is : "+str(k));
		i+=1;
	return render(request,"dailyTasks/date-20210529/program1.html",{'data':lst})






#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------







def onlysum20210531(request):
	if request.method=="POST":
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=a+b
		return render(request,"dailyTasks/date-20210531/onlysum.html",{'result':c})
	return render(request,"dailyTasks/date-20210531/onlysum.html")



#---------------------------------------------------------------------------------------


def checkprime20210531(request):
	if request.method=="POST":
		val=int(request.POST["txtnum1"])
		if(val>1):
			for num in range(2,val):
				if(val%num==0):
					s="It's not a primeNumber, and devided by "+str(num);
					break;
			else:
				s="It's a primeNumber"
		return render(request,"dailyTasks/date-20210531/checkprime.html",{'result':s})
	return render(request,"dailyTasks/date-20210531/checkprime.html")




#---------------------------------------------------------------------------------------


def factorial20210531(request):
	if request.method=="POST":
		value=int(request.POST["txtnum1"])
		calc=1
		for i in range(1,value+1):
			calc*=i;
		return render(request,"dailyTasks/date-20210531/factorial.html",{'result':calc})
	return render(request,"dailyTasks/date-20210531/factorial.html")



#---------------------------------------------------------------------------------------


def middleno20210531(request):
	if request.method=="POST":
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=int(request.POST["txtnum3"])
		if((a>b and a<c) or (a>c and a<b)):
			k=a
		elif((b>a and b<c) or (b>c and b<a)):
			k=b
		else:
			k=c
		return render(request,"dailyTasks/date-20210531/middleno.html",{'result':k})
	return render(request,"dailyTasks/date-20210531/middleno.html")



#---------------------------------------------------------------------------------------


def largestno20210531(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210531/largestno.html",{'result':k})
	return render(request,"dailyTasks/date-20210531/largestno.html")


#---------------------------------------------------------------------------------------



def markseetstudent20210531(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210531/markseetstudent.html",{'result':result})
	return render(request,"dailyTasks/date-20210531/markseetstudent.html")





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------





def markseetstudent20210601(request):
	if request.method=="POST":
		data= {request.POST["txtnum11"]:int(request.POST["txtnum12"]),request.POST["txtnum21"]:int(request.POST["txtnum22"]),request.POST["txtnum31"]:int(request.POST["txtnum32"]),request.POST["txtnum41"]:int(request.POST["txtnum42"]),request.POST["txtnum51"]:int(request.POST["txtnum52"])};
		x=mark=total=0;
		sub=dist='';
		result=[];
		for theKey in data:
			if(not(data.get(theKey)>=0 and data.get(theKey)<=100)):
				result.append("Invalid Mark's.");
				break;
			elif(data.get(theKey)<33):
				x += 1; mark=data.get(theKey); sub += theKey +" ";
			elif(data.get(theKey)>=75):    
				dist += theKey +" ";
			total=total+data.get(theKey)
		else:
			if((x==0) or (x==1 and mark>=28)):   
				if(x==0):      
					per = total/5;
				else:
					per = (total+(33-mark))/5;       
				if(per>=33 and per<45):
					result.append("Pass with Third division "+str(per) + "%")
				elif(per>=45 and per<60):
					result.append("Pass with Second division "+str(per) + "%")
				else:
					result.append("Pass with First Division "+str(per) + "%")
				if(x==1):
					result.append("You are pass by grace and grace mark is "+str(33-mark) + ", subject is "+sub)
				if(not(dist=="")):
					result.append("Distinction subject name are "+dist)
			elif(x==1):
				result.append("supply in "+sub);
			else:
				result.append("failed in "+sub);
		return render(request,"dailyTasks/date-20210601/markseetstudent.html",{'result':result})
	return render(request,"dailyTasks/date-20210601/markseetstudent.html")





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------






def feedback20210602(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210602/feedback.html",{"data":result})  
	return render(request,"dailyTasks/date-20210602/feedback.html")





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------






def assignment120210603(request):
	if request.method=="POST":
		selection = request.POST["selection"]
		p1=float(request.POST["txtnum1"])
		p2=float(request.POST["txtnum2"])
		if(selection=="triangle"):
			result=["Height is "+str(p1),"Base is "+str(p2),"Area of triangle is : "+str((1/2)*p1*p2)]
		elif(selection=="rectangle"):
			result=["Height is "+str(p1),"Width is "+str(p2),"Area of rectangle is : "+str(p1*p2)]
		return render(request,"dailyTasks/date-20210603/assignment1.html",{'value':result,"choice":selection,"txtbox1":request.POST["txtnum1"],"txtbox2":request.POST["txtnum2"]})
	return render(request,"dailyTasks/date-20210603/assignment1.html")


#---------------------------------------------------------------------------------------


def assignment220210603(request):
	if request.method=="POST":
		selection = request.POST["selection"]
		return render(request,"dailyTasks/date-20210603/assignment2.html",{'result':selection})
	selection="None";
	return render(request,"dailyTasks/date-20210603/assignment2.html",{'result':selection})


#---------------------------------------------------------------------------------------



def assignment2sep20210603(request):
	if request.method=="POST":
		selection = request.POST["selection"]
		return render(request,"dailyTasks/date-20210603/assignment2(saperatepage).html",{'result':selection})
	selection="";
	return render(request,"dailyTasks/date-20210603/assignment2(saperatepage).html",{'result':selection})


#---------------------------------------------------------------------------------------



def assignment320210603(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210603/assignment3.html",{'data':lst,'val':k,'select':courses,'choice':selection})
	return render(request,"dailyTasks/date-20210603/assignment3.html")



#---------------------------------------------------------------------------------------



def assignment420210603(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210603/assignment4.html",{'data':Cities,'choice':Country})
	Cities=["empty"];
	return render(request,"dailyTasks/date-20210603/assignment4.html",{'data':Cities})



#---------------------------------------------------------------------------------------



def feedback20210603(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210603/feedback.html",{"data":result,"txtbox1":name,"choice":gender,"select":courses,"feedchoice":feeds,"branch":branches})  
	return render(request,"dailyTasks/date-20210603/feedback.html")



#---------------------------------------------------------------------------------------



def onlysum20210603(request):
	if request.method=="POST":
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=a+b
		return render(request,"dailyTasks/date-20210603/onlysum.html",{'result':c,'txtbox1':request.POST["txtnum1"],'txtbox2':request.POST["txtnum2"]})
	return render(request,"dailyTasks/date-20210603/onlysum.html")



#---------------------------------------------------------------------------------------


def checkprime20210603(request):
	if request.method=="POST":
		val=int(request.POST["txtnum1"])
		if(val>1):
			for num in range(2,val):
				if(val%num==0):
					s="It's not a primeNumber, and devided by "+str(num);
					break;
			else:
				s="It's a primeNumber";
		return render(request,"dailyTasks/date-20210603/checkprime.html",{'result':s,'txtbox1':request.POST["txtnum1"]});
	return render(request,"dailyTasks/date-20210603/checkprime.html");




#---------------------------------------------------------------------------------------


def factorial20210603(request):
	if request.method=="POST":
		value=int(request.POST["txtnum1"])
		calc=1
		for i in range(1,value+1):
			calc*=i;
		return render(request,"dailyTasks/date-20210603/factorial.html",{'result':calc,'txtbox1':request.POST["txtnum1"]})
	return render(request,"dailyTasks/date-20210603/factorial.html")



#---------------------------------------------------------------------------------------


def middleno20210603(request):
	if request.method=="POST":
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=int(request.POST["txtnum3"])
		if((a>b and a<c) or (a>c and a<b)):
			k=a
		elif((b>a and b<c) or (b>c and b<a)):
			k=b
		else:
			k=c
		return render(request,"dailyTasks/date-20210603/middleno.html",{'result':k,'txtbox1':request.POST["txtnum1"],'txtbox2':request.POST["txtnum2"],'txtbox3':request.POST["txtnum3"]})
	return render(request,"dailyTasks/date-20210603/middleno.html")



#---------------------------------------------------------------------------------------


def largestno20210603(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210603/largestno.html",{'result':k,'txtbox1':request.POST["txtnum1"],'txtbox2':request.POST["txtnum2"],'txtbox3':request.POST["txtnum3"]})
	return render(request,"dailyTasks/date-20210603/largestno.html")


#---------------------------------------------------------------------------------------




def markseetstudent20210603(request):
	if request.method=="POST":
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
		return render(request,"dailyTasks/date-20210603/markseetstudent.html",{'result':result,'txtbox11':request.POST["txtnum11"],'txtbox12':request.POST["txtnum12"],'txtbox21':request.POST["txtnum21"],'txtbox22':request.POST["txtnum22"],'txtbox31':request.POST["txtnum31"],'txtbox32':request.POST["txtnum32"],'txtbox41':request.POST["txtnum41"],'txtbox42':request.POST["txtnum42"],'txtbox51':request.POST["txtnum51"],'txtbox52':request.POST["txtnum52"]})
	return render(request,"dailyTasks/date-20210603/markseetstudent.html")





#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------





