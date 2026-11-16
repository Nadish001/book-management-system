from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def registerpage(request):
    if request.method == 'POST':
        form =Registerform(request.POST)
        if form.is_valid():
            usr = form.save()
            Profile.objects.create(user=usr)
            # form.save()
            messages.success(request,"user registered successfully ")
            return redirect(loginpage)
    else:
        form = Registerform()
    return render(request,'registerpage.html',{'form':form})

def loginpage(request):
    if request.method =='POST':
        n1=request.POST.get('n1')
        p1=request.POST.get('p1')
        # print(n1,p1)
        user = authenticate(request,username=n1,password=p1)
        if user:
            login(request,user)
            messages.success(request,"user loggedIn successfully ")
            return redirect(homepage)
        else:
            print("invalid creditential")
    return render(request,'loginpage.html')

def homepage(request):
    return render(request,'homepage.html')

def logoutpage(request):
    logout(request)
    messages.success(request,"user loggedout successfully ")
    return redirect(homepage)

def profilepage(request):
    pro = Profile.objects.get(user = request.user)
    return render(request,'profile.html',{'pro':pro})

def profileedit(request):
    pro = Profile.objects.get(user=request.user)
    if request.method =='POST':
        form = Profileform(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(profilepage)
    else:
        form = Profileform(instance=pro)
    return render(request,'profileedit.html',{"form":form})



def addauthor(request):
    if request.method =='POST':
        form = Authorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(managepage)
    else:
        form = Authorform()
    return render(request,'addauthor.html',{'form':form})
def addbook(request):
    if request.method =='POST':
        form = Bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(managepage)
    else:
        form = Bookform()
    return render(request,'addbook.html',{'form':form})

def dashboard(request):
    return render(request,'dashboard.html')

def managepage(request):
    book = Books.objects.all()
    return render(request,'manage.html',{'book':book})

def viewbook(request,bid):
    book = Books.objects.get(id=bid)
    return render(request, 'viewbook.html', {'book': book})

def editbook(request,bid):
    book = Books.objects.get(id=bid)
    if request.method == 'POST':
        form = Bookform(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect(managepage)
    else:
        form = Bookform(instance=book)
    return render(request, 'editbook.html', {'form': form, 'book': book})

def deletebook(request, bid):
    book =Books.objects.get(id = bid)
    if request.method == 'POST':
        book.delete()
        return redirect(managepage)
    return render(request, 'deletebook.html', {'book': book})