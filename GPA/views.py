from django.db.models import Count
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from GPA.models import GP
import random as rn
from json import dumps
LEFT = ['A','@','C','%','E','?','G','H']
RIGHT = ['!','B','$','D','+','F','"','#']
NUMBERS = [1,2,3,4,5,6,7,8]
parameters = {}
# Create your views here.
def home(request):
    return render(request,'GPA/home.html')

def register(request):
    GP.objects.all().delete()
    if request.method == 'POST':
        name = request.POST.get('NAME')
        phone = request.POST.get('PHONE')
        email = request.POST.get('EMAILID')
        password = request.POST.get('PASSWORD')
        number = request.POST.get('NUMBER')
        object = GP(name = name,phone = phone,email = email,number = number,password = password)
        object.save()
    return render(request,'GPA/register.html')

def login(request):
    global parameters
    global LEFT
    global RIGHT 
    global NUMBERS 
    rn.shuffle(LEFT)
    rn.shuffle(RIGHT)
    params = {'LEFT' : LEFT, 'RIGHT' : RIGHT , 'NUMBERS' : NUMBERS}
    params = {'LEFT' : LEFT, 'RIGHT' : RIGHT , 'NUMBERS' : NUMBERS,'NUM': list(GP.objects.values())[0]['number']}
    for i in range(len(NUMBERS)):
        parameters[i] = {'LEFT':LEFT[i],'RIGHT':RIGHT[i],'NUMBERS':NUMBERS[i]}
    dataJSON = dumps(params)
    dataJSON1 = dumps(parameters)
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == list(GP.objects.values())[0]['password']:
            return redirect(page)
        else:
            messages.error(request, 'Wrong password.')
    return render(request,'GPA/login.html',{'parameters':parameters,'data':dataJSON,'data1':dataJSON1})


# How to submit form without refreshing page
def revise(request):
    params = {0:{'LEFT':'A','RIGHT':'!','NUMBERS':1},1:{'LEFT':'B','RIGHT':'@','NUMBERS':2}}
    if request.method == 'POST':
        name = request.POST.get('name')
        up = request.POST.get('up')
        print(name,up)
    return render(request,'GPA/revise.html',{'params':params})

def email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email == list(GP.objects.values())[0]['email']:
            return redirect(login)
        else:
            messages.error(request, 'Email address is not correct.')
    return render(request,'GPA/email.html')

def page(request):
    return render(request,'GPA/page.html')