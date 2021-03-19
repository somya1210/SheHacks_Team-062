from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
from task.models import Task


def home(request):
    return render(request,'task/homepage.html')
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/userprofile')
        else:
            messages.info(request,'invalidcredential')
            return redirect('/userform')
    else:
     return render(request,'task/userform.html')
def register(request):
    if request.method=='POST':

       username = request.POST['username']
       email = request.POST['email']
       password1 = request.POST['password1']
       password2= request.POST['password2']
       if password1==password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,"USERNAME TAKEN!")
               return redirect('/registration')
           elif User.objects.filter(email=email).exists():
               messages.info(request, "USERNAME TAKEN!")
               return redirect('/registration')
           else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save();
                return redirect('/userform')
       else:
           return redirect('/registration')
           messages.info(request,"PASSWORD NOT MATCHING")
    else:

     return render(request,'task/register.html')

# Create your views here.
def userprofile(request):
    return render(request,'task/userprofile.html')
def challenge(request):
    Tasks=Task.objects.all()

    context={'Tasks':Tasks}
    return render(request,'task/day_challenge.html',context)
def update(request,pk):
    task=Task.objects.get(id=pk,user=request.user)
   # order = Order.objects.create(user=request.user, ordered_date=ordered_date)
    task.completed=True
    task.save()
    return redirect('/userprofile')

def helpline(request):
    return render(request,'task/helpline.html')
def disease(request):
     return render(request,'task/disease.html')
def Team(request):
    return render(request,'task/Team.html')
def doctor(request):
    return render(request,'task/doctor.html')

def progress(request):
    task=Task.objects.all()
    count=0
    for t in task:
        if(t.completed == True):
            count+=1
    rewards=2*count
    context={'count':count,'rewards':rewards}
    return render(request,'task/progress.html',context)