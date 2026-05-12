from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def login_view(request):
  if request.method=="POST":
    username=request.POST['username']   
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
       login(request,user)
       return redirect(reverse('tasks:index'))
    else:
      message='user not exist please try again'
      return render(request,'accounts/login.html',{'message':message})
  return render(request,'accounts/login.html')


def logout_view(request):
  logout(request)
  return redirect('accounts:login')

def signup_view(request):
 
  if request.method=='POST':
      username=request.POST['username']   
      email=request.POST['email']
      password=request.POST['password']
      confirm_password=request.POST['confirm_password']
      if password!=confirm_password:
            message='non identical password enter your password again'
            return render(request,'accounts/signup.html',{'message':message})
      if User.objects.filter(username=username).exists():
            message='the username is taken'
            return render(request,'accounts/signup.html',{'message':message})
      
      user=User.objects.create_user(username=username,email=email,password=password)
      user.save()
      return redirect('accounts:login')
  return render(request,'accounts/signup.html')

def change_password(request):
    if request.method=="POST":
       username=request.POST['username']   
       password=request.POST['password']
       newpassword=request.POST['newpassword']
       try:
         U=User.objects.get(username=username)
       except: 
         message="error"
         return render(request,'accounts/change_password.html',{'message':message})
       
       if U.check_password(password):
          U.set_password(newpassword)
          U.save()
          return redirect('accounts:login')
       else:
          message="your old password is not correct."
          return render(request,'accounts/change_password.html',{'message':message})
        
    return render(request,'accounts/change_password.html')
      