from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,"newAdmin/index.html");

def mapsgmap(request):
	return render(request,"newAdmin/maps-gmap.html");

def mapsvector(request):
	return render(request,"newAdmin/maps-vector.html");


