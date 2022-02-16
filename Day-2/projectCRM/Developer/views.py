from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hey Anshul! You are here, as Developer.");



