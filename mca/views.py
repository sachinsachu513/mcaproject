from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from .form import regform
from.models import registration1


def submitform(request):
      if request.method=='POST':
            if (request.POST.get('first_name')) and request.POST.get('last_name') and request.POST.get('age') and request.POST.get('adress') and request.POST.get('emailid') and request.POST.get('phone') and request.POST.get('password') and request.POST.get('confirm_password'):
                  email = request.POST.get('emailid')
                  if registration1.objects.filter(emailid=email).exists():
                        # return render(request, 'miniproj/
                        return render(request,"miniproj//email.html")
                  registered_number = request.POST.get('phone')
                  if registration1.objects.filter(phonenumber=registered_number).exists():
                        return render(request,'miniproj//phone.html')


                  reg=registration1()
                  reg.first_name=request.POST.get('first_name')
                  reg.last_name=request.POST.get('last_name')
                  reg.age=request.POST.get('age')
                  reg.adress=request.POST.get('adress')
                  reg.emailid=request.POST.get('emailid')
                  reg.phonenumber=request.POST.get('phone')
                  reg.password=request.POST.get('password')
                  y=request.POST.get('confirm_password')

                  if reg.password==y:
                    reg.save()
                  else:
                        return render(request,'miniproj//oops.html')

            else:
                  return HttpResponse ("<h1> some fields are misssing </h1>")
      form=regform()
      return render(request,"miniproj//register.html",context={'form':form})
