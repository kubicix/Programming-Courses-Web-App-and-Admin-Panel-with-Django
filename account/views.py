from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request,"account/login.html",{"error":"Yetkiniz yok."})
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.add_message(request,messages.SUCCESS,"Giriş Başarılı")
            nextUrl=request.GET.get("next",None)
            if nextUrl is None:
                return redirect("index")
            else:
                return redirect(nextUrl)
        else:
            messages.add_message(request,messages.ERROR,"Hatalı kullanıcı adı veya parola.")
            return render(request,"account/login.html")
    else:
        return render(request,"account/login.html")
    
    return render(request,"account/login.html")

def user_register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
        
        if password!=repassword:
            return render(request,"account/register.html",{
                "error":"Passwords doesn't match.",
                "username": username,
                "email": email
                }) 
        
        if User.objects.filter(username=username).exists(): 
            return render(request,"account/register.html",{"error":"User already exists.","username": username,
                "email": email}) 
        
        if User.objects.filter(email=email).exists():  
            return render(request,"account/register.html",{"error":"Email already exists.","username": username,
                "email": email}) 
            
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect("user_login")
    
    else:
        return render(request,"account/register.html")

def user_logout(request):
    messages.add_message(request,messages.SUCCESS,"Çıkış Başarılı.")
    logout(request)
    return redirect("index")