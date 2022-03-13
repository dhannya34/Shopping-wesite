from django.shortcuts import render,redirect
from site_seller.models import *
from site_user.models import *
from django.contrib import messages
from django.http import JsonResponse
from site_admin.models import *
import datetime

# Create your views here.
def sellerregister(request):
    return render(request,'sellerregister.html')
def sellerregisterAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    address=request.POST['address']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
        image="no image"
    user=sellerregister_tb(name=name,gender=gender,dob=dob,country=country,address=address,phone=phone,username=username,password=password,file=image)
    user.save()
    messages.add_message(request,messages.INFO,"Registration Successful")
    return redirect('sellerregister')
def checkUsername1(request):
    username=request.GET['username']
    user=register_tb.objects.filter(username=username)
    seller=sellerregister_tb.objects.filter(username=username)
    if len(seller)>0:
        msg="exists"
    elif len(user)>0:
        msg="exists"
    else:
        msg="not exists"
    return JsonResponse({'valid':msg})
def addproduct(request):
    user=catagory_tb.objects.all()
    return render(request,'addproduct.html',{'data':user})
def addproductAction(request):
    productname=request.POST['productname']
    price=request.POST['price']
    details=request.POST['details']
    stock=request.POST['stock']
    catagoryid=request.POST['catagory']
    catagory_obj=catagory_tb.objects.get(id=catagoryid)
    
    sellerid=request.session['id']
    seller_obj=sellerregister_tb.objects.get(id=sellerid)
    
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
        image="no image"
    seller=product_tb(productname=productname,price=price,details=details,stock=stock,catagoryid=catagory_obj,sellerid=seller_obj,file=image)
    seller.save()
    messages.add_message(request,messages.INFO,"Added Successfull")
    return redirect('addproduct')
def viewProducts(request):
    uid=request.session['id']
    uid_obj=sellerregister_tb.objects.get(id=uid)
    user=product_tb.objects.filter(sellerid=uid_obj)
    return render(request,'viewProducts.html',{'data':user})
def delete(request,uid):
    
    user=product_tb.objects.filter(id=uid).delete()
    return redirect('viewProducts')
def editp(request,uid):
    catag=catagory_tb.objects.all()
    product=product_tb.objects.filter(id=uid)
    return render(request,'editp.html',{'data':product,'catagory':catag})
def updateeditp(request):
    
    productid=request.POST['productid']
    productidd=product_tb.objects.filter(id=productid)
    productname=request.POST['productname']
    price=request.POST['price']
    details=request.POST['details']
    stock=request.POST['stock']
    if len(request.FILES)>0:
        image=request.FILES['file']
        print(image)
    else:
        image=productidd[0].file
        print(image)

    catagory=request.POST['catagory']
    catagory_obj=catagory_tb.objects.get(id=catagory)
    product=product_tb.objects.filter(id=productid).update(productname=productname,price=price,details=details,stock=stock,catagoryid=catagory_obj)
    product_obj=product_tb.objects.get(id=productid)
    product_obj.file=image
    product_obj.save()
    messages.add_message(request,messages.INFO,"Updated Successfully")
    return redirect('viewProducts')
def updateProfile(request):
    uid=request.session['id']
    user=sellerregister_tb.objects.filter(id=uid)
    return render(request,'updateProfile.html',{'data':user})
def updateProfileAction(request):
    
    uid=request.session['id']
    uidd=sellerregister_tb.objects.filter(id=uid)
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    address=request.POST['address']
    phone=request.POST['phone']
    username=request.POST['username']
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
        image=uidd[0].file
    seller=sellerregister_tb.objects.filter(id=uid).update(name=name,gender=gender,dob=dob,country=country,address=address,phone=phone,username=username)
    seller_obj=sellerregister_tb.objects.get(id=uid)
    seller_obj.file=image
    seller_obj.save()
    messages.add_message(request,messages.INFO,"Updated Successfully")
    return redirect('updateProfile')
def viewcustomerorders(request):
    uid=request.session['id']
    seller=order_tb.objects.filter(sellerid=uid)
    return render(request,'viewcustomerorders.html',{'data':seller})
def accept(request,uid):
    seller=order_tb.objects.filter(id=uid).update(status='Accepted')
    return redirect('viewcustomerorders')
def rejecto(request,uid):
    seller=order_tb.objects.filter(id=uid).update(status='Rejected'),
    return redirect('viewcustomerorders')
def cnfmcncltn(request,uid):
    seller=order_tb.objects.filter(id=uid).update(status='Cancellation Successfull')
    order=order_tb.objects.filter(id=uid)
    pstock=order[0].productid.stock
    quantity=order[0].quantity    
    pstock1=pstock+quantity
    seller1=product_tb.objects.filter(id=order[0].productid.id).update(stock=pstock1)
    return redirect('viewcustomerorders')
def trackorder(request,uid):
    seller=order_tb.objects.filter(id=uid)
    return render(request,'trackorder.html',{'data':seller})
def trackingAction(request):
    orderid=request.POST['trackingid']
    orderid_obj=order_tb.objects.get(id=orderid)
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    details=request.POST['details']
    detailsupper=details.upper()
    if 'DELIVERED' in detailsupper:
        seller=order_tb.objects.filter(id=orderid).update(status='Delivered')
    seller=tracking_tb(date=date,time=time,orderid=orderid_obj,details=details)
    seller.save()
    
    return redirect('viewcustomerorders')

    
    

    
    
    

    
