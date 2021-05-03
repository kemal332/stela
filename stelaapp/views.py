from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(response):
    return render(response, "stelaapp/index.html")

def login(response):
    return render(response, "stelaapp/login.html")

def register(response):
    return render(response, "stelaapp/register.html")

def reset(response):
    return render(response, "stelaapp/reset.html")

