# from django.http import HttpResponse(for checking)
from django.shortcuts import render

def home(request):
    return render(request,'home.html')