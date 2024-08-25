from django.shortcuts import render,HttpResponseRedirect
from .forms import UserRegistration
from .models import Registration
from django.contrib import messages
# Create your views here.


def addandshow(request):
    if request.method == "POST":
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            ps = fm.cleaned_data["password"]
            rs = fm.cleaned_data["reenter_Password"]
            reg = Registration(name = nm,email=em,password=ps,reenter_Password=rs)
            reg.save()
            messages.add_message(request,messages.SUCCESS,"Thanks For Registration")
            fm = UserRegistration()


        
    else:
        fm = UserRegistration()
    stud = Registration.objects.all()

    return render(request, 'enroll/addandshow.html',{"form":fm,"stu":stud})

def update_data(request,id):
    if request.method == "POST":
        pi = Registration.objects.get(pk =id)
        fm = UserRegistration(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = Registration.objects.get(pk =id)
        fm = UserRegistration( instance = pi)

    return render(request, 'enroll/update.html',{'form':fm })






def delete_data(request,id):
    if request.method == "POST":
        pi = Registration.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect("/")


