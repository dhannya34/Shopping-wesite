"""sample_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from site_admin import views as adminview
from site_seller import views as sellerview
from site_user import views as userview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',userview.index,name='index'),
    url(r'^register/$',userview.register,name='register'),
    url(r'^registerAction/$',userview.registerAction,name='registerAction'),
    url(r'^sellerregister/$',sellerview.sellerregister,name='sellerregister'),
    url(r'^sellerregisterAction/$',sellerview.sellerregisterAction,name='sellerregisterAction'),
    url(r'^login/$',userview.login,name='login'),
    url(r'^loginAction/$',userview.loginAction,name='loginAction'),
    url(r'^ViewAllusers/$',adminview.ViewAllusers,name='ViewAllusers'),
    url(r'^checkUsername1/$',sellerview.checkUsername1,name='checkUsername1'),
    url(r'^AddCatagory/$',adminview.AddCatagory,name='AddCatagory'),
    url(r'^AddCatagoryAction/$',adminview.AddCatagoryAction,name='AddCatagoryAction'),
    url(r'^edit/$',userview.edit,name='edit'),
    url(r'^editAction/$',userview.editAction,name='editAction'),
    url(r'^approve/(?P<uid>\d+)/$',adminview.approve,name='approve'),
    url(r'^reject/(?P<uid>\d+)/$',adminview.reject,name='reject'),
    url(r'^addproduct/$',sellerview.addproduct,name='addproduct'),
    url(r'^addproductAction/$',sellerview.addproductAction,name='addproductAction'),
    url(r'^viewProducts/$',sellerview.viewProducts,name='viewProducts'),
    url(r'^delete/(?P<uid>\d+)/$',sellerview.delete,name='delete'),
    url(r'^editp/(?P<uid>\d+)/$',sellerview.editp,name='editp'),
    url(r'^updateeditp/$',sellerview.updateeditp,name='updateeditp'),
    url(r'^viewuserProducts/$',userview.viewuserProducts,name='viewuserProducts'),
    url(r'^updateProfile/$',sellerview.updateProfile,name='updateProfile'),
    url(r'^updateProfileAction/$',sellerview.updateProfileAction,name='updateProfileAction'),
    url(r'^addtocart/(?P<uid>\d+)/$',userview.addtocart,name='addtocart'),
    url(r'^addtocartAction/$',userview.addtocartAction,name='addtocartAction'),
    url(r'^viewcart/$',userview.viewcart,name='viewcart'),
    url(r'^deletep/(?P<uid>\d+)/$',userview.deletep,name='deletep'),
    url(r'^viewcartAction/$',userview.viewcartAction,name='viewcartAction'),
    url(r'^vieworders/$',userview.vieworders,name='vieworders'),
    url(r'^cancel/(?P<uid>\d+)/$',userview.cancel,name='cancel'),
    url(r'^viewcustomerorders/$',sellerview.viewcustomerorders,name='viewcustomerorders'),
    url(r'^accept/(?P<uid>\d+)/$',sellerview.accept,name='accept'),
    url(r'^rejecto/(?P<uid>\d+)/$',sellerview.rejecto,name='rejecto'),
    url(r'^cnfmcncltn/(?P<uid>\d+)/$',sellerview.cnfmcncltn,name='cnfmcncltn'),
    url(r'^trackorder/(?P<uid>\d+)/$',sellerview.trackorder,name='trackorder'),
    url(r'^trackingAction/$',sellerview.trackingAction,name='trackingAction'),
    url(r'^trackorder1/(?P<uid>\d+)/$',userview.trackorder1,name='trackorder1'),
    url(r'^searchproducts/$',userview.searchproducts,name='searchproducts'),
    url(r'^searchAction/$',userview.searchAction,name='searchAction'),
    url(r'^searchprobycatandpri/$',userview.searchprobycatandpri,name='searchprobycatandpri'),
    url(r'^searchprobycatandpriAction/$',userview.searchprobycatandpriAction,name='searchprobycatandpriAction'),
    url(r'^logout/$',userview.logout,name='logout'),
    url(r'^forgotpassword/$',userview.forgotpassword,name='forgotpassword'),
    url(r'^forgotAction/$',userview.forgotAction,name='forgotAction'),
    url(r'^forgotpassAction/$',userview.forgotpassAction,name='forgotpassAction'),
    url(r'^confirmationpasswordAction/$',userview.confirmationpasswordAction,name='confirmationpasswordAction'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
