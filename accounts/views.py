from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse 
from django.contrib.auth import authenticate, login
# Create your views here.


def userdashboard(request):
    return render(request,'userdashboard.html')
 
def index(request):
    if request.POST.get("form_one"):
        if not User.objects.filter(email=request.POST["email"]).exists():
            data=User()
            data.password = request.POST["password"]
            data.confirm=request.POST["confirm"]
            data.first_name=request.POST["first_name"]
            data.last_name=request.POST["last_name"]
            data.username=request.POST["username"]
            data.email = request.POST["email"]
            data.is_active = True
            if data.password == data.confirm:
                print("user craeted")
                data.save()
                return redirect("userdashboard")
            else:
                print("wrong password")
                return redirect("index")
        else:
            print("email exixsts")
            return redirect("index") 
    elif request.POST.get("form_two"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print('welcome')
            return redirect('userdasboard')	
        else:
            print('wrong input ')
            return redirect('index')
    else:
        return render(request,"index.html")