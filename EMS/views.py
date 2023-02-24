from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from EMS.models import *

# Create your views here.

def view_add(request):
   if request.method=='GET':
      resp=render(request,'EMS/crud.html')
      return resp
   elif "btn_add" in request.POST:
      stu=Student()
      stu.name=request.POST.get('t1','N.A')
      stu.age=int(request.POST.get('agee',0))
      stu.mobileno=request.POST.get('m1','N.A')
      stu.city=request.POST.get('city','N.A')
      stu.save()
      resp=HttpResponse('<h1>RESPONSE STORED SUCCESSFULLY!!!</h1>')
      return resp
   elif "btn_search" in request.POST:
      sid=int(request.POST.get('i1',0))
      alldet=Student.objects.get(id=sid)
      dict={"stu":alldet}
      resp=render(request,'EMS/crud.html',context=dict)
      return resp
   elif 'btn_modify' in request.POST:
      stu=Student()
      stu.id=int(request.POST.get('i1',0))
      if Student.objects.filter(id=stu.id).exists():
         stu.name=request.POST.get('t1','N.A')
         stu.age=int(request.POST.get('agee',0))
         stu.mobileno=request.POST.get('m1','N.A')
         stu.city=request.POST.get('city','N.A')
         stu.save()
         resp=HttpResponse('<h1>RESPONSE MODIFIED SUCCESSFULY!!!</h1>')
         return resp
      
   elif 'btn_delete' in request.POST:
      sid=int(request.POST.get('i1',0))
      Student.objects.filter(id=sid).delete()
      resp=HttpResponse('<h1>RESPONSE DELETED SUCCESSFULLY!!!</h1>')
      return resp

   elif 'btn_show' in request.POST:
      alldet=Student.objects.all()
      dict={"alldet":alldet}
      resp=render(request,'EMS/crud.html',context=dict)
      return resp




def payment_details(request):
    if request.method=="GET":
        resp=render(request,'EMS/payment_det.html')
        return resp
    elif request.method=="POST":
        dict1={}
        #if "pbtn" in request.POST:
        try:
            sid=int(request.POST.get("ptext",0))
            stu=Student.objects.get(id=sid)
            allp=stu.paymentdetails_set.all()
            dict1={"allp":allp,"stu":stu}
            resp=render(request,'EMS/payment_det.html',context=dict1)
            return resp
        except Student.DoesNotExist:
            dict1["msg"]="Student Does Not Exist"
            resp=render(request,'EMS/payment_det.html',context=dict1)
            return resp

def Course_Wise_Student_Det(request):
    allc=Course.objects.all()
    dict={"allc":allc}
    if request.method=="GET":
        c=Course.objects.get(id=1)
        cidd=c.id
        cname=c.name
        dict["cidd"]=cidd
        dict["cname"]=cname
        studet=c.students.all()
        dict["studet"]=studet
        resp=render(request,"EMS/Coursee_det.html",context=dict)
        return resp
    elif request.method=="POST":
        cid=int(request.POST.get("slc",0))
        c=Course.objects.get(id=cid)
        cidd=c.id
        cname=c.name
        dict["cidd"]=cidd
        dict["cname"]=cname
        studet=c.students.all()
        dict["studet"]=studet
        resp=render(request,"EMS/Coursee_det.html",context=dict)
        return resp


   



