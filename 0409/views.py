from django.shortcuts import render
from django.http import HttpResponse

#create your views here
def index(request):
	return HttpResponse("hello mom I'm here!")
# Create your views here.
