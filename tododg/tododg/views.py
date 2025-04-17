from django . shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tododg import models
from tododg.models import TODOO


def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm, emailid, pwd)
        my_user=User.objects.create_user(fnm, emailid, pwd)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')


def loginn(requset):
    if requset.method == 'POST':
        fnm=requset.POST.get('fnm')
        pwd=requset.POST.get('pwd')
        print(fnm, pwd)
        userr=authenticate(requset,username=fnm,password=pwd)
        if userr is not None:
            login(requset, userr)
            return redirect('/todopage')
        else:
            redirect('/loginn')
    return render(requset, 'loginn.html')