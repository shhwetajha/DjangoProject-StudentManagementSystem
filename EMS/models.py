
from django.db import models
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    dob=models.DateField(null=True,blank=True)
    mobileno=models.CharField(max_length=20)
    city=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    last_modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=50)
    students=models.ManyToManyField(Student,null=True,blank=True)
    def __str__(self):
        return self.name

class PaymentDetails(models.Model):
    amount=models.IntegerField()
    payment_mode=models.CharField(max_length=100,choices=[('Debit Card','Debit Card'),('Credit Card','Credit Card'),('Cash','Cash'),('paytm','paytm')])
    payment_date=models.DateTimeField(auto_now=True)
    student=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    

