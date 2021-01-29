from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import HttpResponse 
from django.contrib.auth import authenticate, login
# Create your views here.


def userdashboard(request):
    return render(request,'userdashboard.html')
 
def index(request):
    if request.POST.get("form_one"):
        
            data=User()
            data.password=make_password(request.POST["password"])
            data.first_name=request.POST["first_name"]
            data.last_name=request.POST["last_name"]
            data.username=request.POST["username"]
            data.email = request.POST["email"]
            data.is_active = True
            print("user craeted")
            data.save()
            return redirect("userdashboard")
                 
    elif request.POST.get("form_two"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print('welcome')
            return redirect('userdashboard')	
        else:
            print('wrong input ')
            return redirect('index')
    else:
        return render(request,"index.html")