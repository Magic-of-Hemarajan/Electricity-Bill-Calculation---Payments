from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ElectricityApp.models import payments
from django.contrib import messages
import datetime
import random

# Create your views here.

def index_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            # return HttpResponse("username is already exits")
            messages.error(request,"**Username already exits")
            return redirect('/')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request,'base.html')

def Login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password")
    return render(request,'login.html')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

def Due_calculation(request):
    return render(request, 'calculation.html')

@login_required(login_url='/login/')
def payments_view(request):
    users = request.user
    if request.method == 'POST':
        number = request.POST.get('consumer-number')
        name = request.POST.get('consumer-name')
        unit = request.POST.get('units')
        price = request.POST.get('priceing')
        receipt = random.randint(0,999999999)
        date = datetime.date.today()
        uname = User.objects.get(username=users)
        
        pay = payments(username=uname, number=number, name=name, unit=unit, price=price, receipt=receipt, date=date)
        pay.save()
        request.session['payments']=receipt
        return render(request,'pages.html',{'receipt':receipt})

    return render(request,'newpay.html')

def generate(request):
    if request.method == 'POST':
        bill = request.POST.get('bills-cus')
        try:
            bills = payments.objects.get(receipt=bill)
        except payments.DoesNotExist:
            return HttpResponse('<script>alert("receipt number not found");window.location.href=""</script>')
        type = "online"
        context={
            'bills':bills,
            'type':type,
        }
        return render(request,'bills-print.html',context)
    return render(request,'payments.html')

def logout_view(request):
    logout(request)
    return redirect('index')
