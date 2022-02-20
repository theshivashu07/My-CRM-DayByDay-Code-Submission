from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"proManager/index.html");
 
def about(request):
	return render(request,"proManager/about.html");

def contact(request):
	return render(request,"proManager/contact.html");

def gym(request):
	return render(request,"proManager/gym.html");

def price(request):
	return render(request,"proManager/price.html");

def login(request):
	return render(request,"proManager/login.html");

'''
def masters(request):
	return HttpResponse("Hey Shivashu! You are here, as Project Manager. and this is masters");
'''
