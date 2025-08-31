from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *





def loginpage(request):
    
    if request.user.is_authenticated:

        return redirect("hospital_info")#when we close the tab without proper logout again we when we enter into the website it does not take you to login page rather it takes you to given path.
    else:

        context={
            "message" : ""

    }

    if request.method == "POST":

        auth_member = authenticate(username=request.POST["username"],password = request.POST["password"])

        print(auth_member)

        if auth_member is not None:

            login(request,auth_member)

            return redirect("hospital_info") 


                    
        else:

            context={
                "message" : "**Invalid Username or Password"
            }

            return render(request,"auth_page/login.html",context)
        
    return render(request,"auth_page/login.html",context)





def Logoutpage1(request):
    logout(request)
    return redirect("auth_page:login")




def registerpage(request):
    context={
    "message" : ""
}
    if request.method == "POST":
        exist_user = User.objects.filter(username=request.POST["username"])

        if len(exist_user) >0:

            context={
                "message" : "** User Already Exists !"
            }



        else:
            add_user = User(username=request.POST["username"], 
                            email=request.POST["email"],location=request.POST["location"],mobile_number=request.POST["mobile"],parent_name=request.POST["parent_name"],
                            aadhaar_number=request.POST["aadhaar_number"])
                            
            
            add_user.set_password(request.POST["password"])


            add_user.save()

            
            return redirect('auth_page:login')

    
        
    return render(request,"auth_page/register.html",context)
