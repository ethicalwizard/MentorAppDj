from django.shortcuts import render
from django.http import HttpResponse

def login_as (request):
    return render(request,"login_as_page.html")

def login(request):
    return render(request,"Login.html")