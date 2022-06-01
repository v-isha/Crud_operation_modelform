from django.shortcuts import redirect, render 
from django.http import HttpResponseRedirect ,HttpResponse
from .forms import customerregistration
from .models import customer

# Create your views here.
def land(request):
    return render(request,"reg/land.html")

# this function will save and show data
def index(request):
    
    if request.method =="POST":
       cr=customerregistration(request.POST)
       if cr.is_valid():
         id = cr.cleaned_data["customer_id"]
         nm = cr.cleaned_data["name"]
         eml = cr.cleaned_data["email"]
         pss = cr.cleaned_data["password"]
         cus =customer(customer_id =id,name=nm,email=eml,password=pss)
         cus.save()
         cr=customerregistration()
        #  return render(request,"reg/land.html")
         
    else:
        
        cr=customerregistration()
        getdata = customer.objects.all()
    return render(request,"reg/index.html",{'form':cr ,"cus":getdata})
    
# data display
# def showdata(request):
#       crd = customer.objects.all()
#       return render(request,"reg/index.html",{'cus':crd})


# this function for update
def userupdate(request,id):
    if request.method =="POST":
        cus = customer.objects.get(pk=id)
        pi=customerregistration(request.POST,instance=cus)
        if pi.is_valid():
            nm = pi.cleaned_data["name"]
            eml = pi.cleaned_data["email"]
            pss = pi.cleaned_data["password"]
            cupi =customer(customer_id =id,name=nm,email=eml,password=pss)
            cupi.save()
            return HttpResponseRedirect('/index/') 
    else:
        cus = customer.objects.get(pk=id)
        pi=customerregistration(instance=cus)
    return render(request,"reg/update.html",{'form':pi})

# delete function
def userdel(request,id):
    if request.method =="POST":
      cus = customer.objects.get(pk=id)
      cus.delete()
      return HttpResponseRedirect('/index/')
