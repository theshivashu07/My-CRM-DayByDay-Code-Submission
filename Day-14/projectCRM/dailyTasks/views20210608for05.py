from django.shortcuts import render
from django.http import HttpResponse





#---------------------------------------------------------------------------------------
def calcEMIdirect(request):
	return render(request,"dailyTasks/date-20210608for05/calculatorEMI.html")

#---------------------------------------------------------------------------------------
def calcEMI(request):
	return render(request,"dailyTasks/date-20210608for05/calcEMI.html")

#---------------------------------------------------------------------------------------
def calcCovid(request):
	if request.method=="POST":
		age = request.POST["age"]
		HealthIssues = request.POST.getlist("HealthIssues[]")
		covidSymptoms =request.POST.getlist("covidSymptoms[]")
		if(age=='one' or age=='four' or age=='five'):
			if(len(HealthIssues)>2 and len(covidSymptoms)>2):
				msg="High Risk"
			else:
				msg="Medium Risk"
		if(('Nothing' in HealthIssues) or ('Nothing' in covidSymptoms)):
			msg="Low Risk";
		else:
			msg="No Risk";
		return render(request,"dailyTasks/date-20210608for05/calcCovid.html",{"msg":msg})
	return render(request,"dailyTasks/date-20210608for05/calcCovid.html")


