from tkinter import X
from django.shortcuts import render
from django.http import JsonResponse
from . import Pool

def login(request):
    return render(request,'login.html')

def CheckUserLogin(request):   
    try:
        DB,CMD= Pool.ConnectionPooling()
        email= request.POST['email']
        # phone= request.POST['phone']
        password=request.POST['password']
        Q="select * from signup where email='{0}'and password='{1}'".format(email,password)
        CMD.execute(Q)
        row= CMD.fetchone()
        print(row)
        DB.commit()
       
        if(row):
             return render(request,'index.html',{'UserData':row})
        else:
            return render(request, 'login.html', {'message': 'Invalid Credentails'})
        DB.close()
        
    except Exception as e:
        print(e)
        return render(request,"login.html",{'message':'Something went wrong!'})