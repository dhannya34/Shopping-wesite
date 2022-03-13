from django.shortcuts import render,redirect
from site_user.models import *
from site_admin.models import *
from site_seller.models import *
from django.contrib import messages
from django.http import JsonResponse
import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')
def registerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    address=request.POST['address']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb(name=name,gender=gender,dob=dob,country=country,address=address,phone=phone,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"REGISTRATION SUCCESSFUL")
    return redirect('register')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(username=username,password=password)
    admin=adminregister_tb.objects.filter(username=username,password=password)
    seller=sellerregister_tb.objects.filter(username=username,password=password)
    if user.count()>0:
        request.session['id']=user[0].id
        return render(request,'userhome.html')
    elif admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,'adminhome.html')
    elif seller.count()>0:
        request.session['id']=seller[0].id
        if seller[0].status == 'approved':
            return render(request,'sellerhome.html')
        else:
            messages.add_message(request,messages.INFO,"Not Approved")
            return redirect('login')
    else:
        messages.add_message(request,messages.INFO,"Incorrect username or password")
        return redirect('login')
def edit(request):
    uid=request.session['id']
    user=register_tb.objects.filter(id=uid)
    return render(request,'edit.html',{'data':user})
def editAction(request):
    uid=request.session['id']
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    address=request.POST['address']
    phone=request.POST['phone']
    username=request.POST['username']
    user=register_tb.objects.filter(id=uid).update(name=name,gender=gender,dob=dob,country=country,address=address,phone=phone,username=username)
    messages.add_message(request,messages.INFO,"Updated Successfully")
    return redirect('edit')
def viewuserProducts(request):
    user=product_tb.objects.all()
    return render(request,'viewuserProducts.html',{'data':user})
def addtocart(request,uid):
    productid=uid
    user=product_tb.objects.filter(id=uid)
    return render(request,'addtocart.html',{'data':user,'product':productid})
def addtocartAction(request):
    uid=request.session['id']
    uid_obj=register_tb.objects.get(id=uid)
    productid=request.POST['productid']
    print(productid)
    productid_obj=product_tb.objects.get(id=productid)
    pstock=productid_obj.stock
    print(pstock)
    productprice=request.POST['price']
    shippingaddress=request.POST['shippingaddress']
    contactno=request.POST['contactno']
    quantity=request.POST['quantity']
    print(quantity)
    totalprice=request.POST['totalprice']
    
    if int(pstock)<int(quantity):
        messages.add_message(request,messages.INFO,"Entered quantity more and not available")
    else:
        user=cart_tb(productid=productid_obj,userid=uid_obj,shippingaddress=shippingaddress,contactno=contactno,quantity=quantity,totalprice=totalprice)
        user.save()
        messages.add_message(request,messages.INFO,"Product added to cart")
    return redirect('viewuserProducts')
def viewcart(request):
    user=cart_tb.objects.all()
    return render(request,'viewcart.html',{'data':user})
def deletep(request,uid):
    user=cart_tb.objects.filter(id=uid).delete()
    return redirect('viewcart')
def viewcartAction(request):
    uid=request.session['id']
    checkbox=request.POST.getlist('checkbox')
    for pid in checkbox:
        product=cart_tb.objects.filter(id=pid)
        userid=request.session['id']
        userid_obj=register_tb.objects.get(id=userid)
        selleridd=product[0].productid.sellerid.id
        sellerid_obj=sellerregister_tb.objects.get(id=selleridd)
        pstock=product[0].productid.stock
        shippingaddress=product[0].shippingaddress
        quantity=product[0].quantity
        totalprice=product[0].totalprice
        productid=product[0].productid.id
        productid_obj=product_tb.objects.get(id=productid)
        date=datetime.date.today()
        time=datetime.datetime.now().strftime("%H:%M")
        if int(pstock)<int(quantity):
            messages.add_message(request,messages.INFO,"Entered quantity more and not available")
        else:
            user=order_tb(productid=productid_obj,userid=userid_obj,sellerid=sellerid_obj,shippingaddress=shippingaddress,quantity=quantity,totalprice=totalprice,date=date,time=time)
            user.save()
            stock1=int(pstock)-int(quantity)
            user1=product_tb.objects.filter(id=productid).update(stock=stock1)
            product.delete()
            messages.add_message(request,messages.INFO,"Product Successfully placed")
        return redirect('viewcart')
def vieworders(request):
    uid=request.session['id']
    user=order_tb.objects.filter(userid=uid)
    print(user)
    return render(request,'vieworders.html',{'data':user})
def cancel(request,uid):
    
    user=order_tb.objects.filter(id=uid).update(status='cancelled')
    return redirect('vieworders')
def trackorder1(request,uid):
    user=tracking_tb.objects.filter(orderid=uid)
    return render(request,'trackorder1.html',{'data':user})
def searchproducts(request):
    return render(request,'searchproducts.html')
def searchAction(request):
    search=request.POST['search']
    product=product_tb.objects.filter(productname__istartswith=search)
    return render(request,'viewuserProducts.html',{'data':product})
def searchprobycatandpri(request):
    
    user=catagory_tb.objects.all()
    return render(request,'searchprobycatandpri.html',{'data':user})
def searchprobycatandpriAction(request):
    
    catagory=request.POST['catagory']
    price=request.POST['price']
    search1=product_tb.objects.filter(price__lte=price,catagoryid=catagory)
    print(search1)
    return render(request,'viewuserProducts.html',{'data':search1})
def logout(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,"Logged out")
    return render(request,'login.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotAction(request):
    username=request.POST['username']
    user=register_tb.objects.filter(username=username)
    admin=adminregister_tb.objects.filter(username=username)
    seller=sellerregister_tb.objects.filter(username=username)
    if user.count()>0:
        return render(request,'forgotAction.html')
    elif admin.count()>0:
        return render(request,'forgotAction.html')
    elif seller.count()>0:
        return render(request,'forgotAction.html')
    else:
        messages.add_message(request,messages.INFO,"Username doesn't match")
        return redirect('forgotpassword')

def forgotpassAction(request):
    dob=request.POST['dob']
    phoneno=request.POST['phone']
    country=request.POST['country']
    user=register_tb.objects.filter(dob=dob,phone=phoneno,country=country)
    seller=sellerregister_tb.objects.filter(dob=dob,phone=phoneno,country=country)
    if user.count()>0:
        return render(request,'cofirmationpassword.html',{'data':user})
    elif seller.count()>0:
        return render(request,'cofirmationpassword.html',{'data':seller})
    else:
        messages.add_message(request,messages.INFO,"Dob,phone or country doesn't match")
        return render(request,'forgotAction.html')
def confirmationpasswordAction(request):
    userid=request.POST['username']
    newpassword=request.POST['newpassword']
    confpassword=request.POST['confpassword']
    if newpassword == confpassword:
        user=register_tb.objects.filter(username=userid).update(password=newpassword)
        seller=sellerregister_tb.objects.filter(username=userid).update(password=newpassword)
        messages.add_message(request,messages.INFO,"Password Successfully Reset")
        return redirect('login')
    else:
        messages.add_message(request,messages.INFO,"Entered newpassword and confirmed password not same")
        return render(request,'cofirmationpassword.html',{'data':userid})
    

    
    







































        
        
        
        
        
    

 
        

    
