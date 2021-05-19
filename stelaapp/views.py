from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(response):
    return render(response, "stelaapp/index.html")

