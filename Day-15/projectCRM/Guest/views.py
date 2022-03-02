from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"Guest/index.html");
 
def about(request):
	return render(request,"Guest/about.html");

def contact(request):
	return render(request,"Guest/contact.html");

def gym(request):
	return render(request,"Guest/gym.html");

def price(request):
	return render(request,"Guest/price.html");

