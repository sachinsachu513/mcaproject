from django.http import HttpResponse
from django.shortcuts import render
from.models import samapletable,submitform
from .forms import registerform,myform,registerf
# Create your views here.
def getstudent(request):
    student=samapletable.objects.all()
    return render(request,"details.html",context={"student":student})
def greetings(request):
    return render(request,"greetings.html")

def register(request):
    form=registerform()
    return render(request,"registerform.html",context={"form":form})

def allforms(request):
    form=myform()
    return render(request,"registerform.html",context={"form":form})

def submitform1(request):
     if request.method=='POST':
        if (request.POST.get('first_name') and request.POST.get("age") and request.POST.get("emailid") and request.POST.get("adress")):
           reg=submitform()
           reg.first_name=request.POST.get("first_name")
           reg.age=request.POST.get("age")
           reg.emailid=request.POST.get("emailid")
           reg.adress=request.POST.get("adress")
           reg.save()
        else:
            return HttpResponse("<h1>some fields are missing <h1>")

     form=registerf()
     return render(request,"register1.html",context={'form':form})

def getting(request):
    details=submitform.objects.all()
    return render(request,'databse.html',context={'details':details})