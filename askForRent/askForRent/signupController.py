from tkinter import X
from django.shortcuts import render
from django.http import JsonResponse
from . import Pool

def signup(request):
    return render(request,'signup.html')
def Submit_User(request):   #this action will sumbit the Categories to the database which is filled by the user
    try:
        DB,CMD= Pool.ConnectionPooling()
        username= request.POST['username']
        email= request.POST['email']
        phone= request.POST['phone']
        password= request.POST['password']
        confirmpassword= request.POST['confirmpassword']
        Q="insert into signup(email,name,phone,password,confirmpassword) values('{0}','{1}',{2},'{3}','{4}')".format(email,username,phone,password,confirmpassword)
        # print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request,'index.html')
    except Exception as e:
        print("Error: ",e)
        return render(request, 'signup.html', {'message': 'Registration Failed!'})
