from django.shortcuts import render,redirect
from site_seller.models import *
from site_admin.models import *
from django.contrib import messages
# Create your views here.


def ViewAllusers(request):
    user=sellerregister_tb.objects.all()
    return render(request,'ViewAllusers.html',{'data':user})
def AddCatagory(request):
    return render(request,'AddCatagory.html')
def AddCatagoryAction(request):
    catagoryname=request.POST['catagoryname']
    cata=catagory_tb(catagory=catagoryname)
    cata.save()
    messages.add_message(request,messages.INFO,"Added Successfully")
    return redirect('AddCatagory')
def approve(request,uid):
    user=sellerregister_tb.objects.filter(id=uid).update(status="approved")
    return redirect('ViewAllusers')
def reject(request,uid):
    user=sellerregister_tb.objects.filter(id=uid).update(status="rejected")
    return redirect('ViewAllusers')
def Adminhome(request):
    return render(request,'adminhome.html')
