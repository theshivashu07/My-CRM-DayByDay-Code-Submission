from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hey Sushma! You are here, as Client.");



