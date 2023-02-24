from django.urls import path
from .views import *
#http://127.0.0.1:8000/ems/
urlpatterns=[
    path('add/',view_add, name='add'),
    path('payment/',payment_details ,name='payment'),
    path('Coursedet/',Course_Wise_Student_Det,name="course"),
    
]

