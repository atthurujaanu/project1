from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first1(request):
    return HttpResponse('this is app2-first fuction')
