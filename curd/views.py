from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import employees
from .forms import employeform
def getemploy(request):
    emp=employees.objects.all()
    return render(request,"curd//empdata.html",context={"emp":emp})


def createmploy(request):
    form=employeform()
    if request.method=='POST':
        form=employeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse ("<h1>new employ data added sucessfully</h1>")
    return render(request,'curd//addemp.html',context={"form":form})
def deleteemploy(request,id):
    emp=employees.objects.get(id=id)
    emp.delete()
    return redirect("/curd/curd1")

def updateemploy(request,id):
    emp=employees.objects.get(id=id)
    if request.method=='POST':
        form=employeform(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponse("""
            <h2>employ data was added successfully<h1>
            <h2><a href="/curd/curd1/">
            <h3> click here </a> employdetails</h2>
            
            
            
            """)

    return render(request,"curd//update.html",context={'emp':emp})