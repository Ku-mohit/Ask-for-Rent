from tkinter import X
from django.shortcuts import render
from django.http import JsonResponse
from . import Pool

def Index(request):
    return render(request,'index.html')
