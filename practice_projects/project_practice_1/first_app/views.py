from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
   
    d={'Name':"Arpan",'age':22 ,'slash':"I'm Arpan" ,'datetime':datetime.datetime.now(),'listDic':[{'name': 'zed', 'age': 19},{'name': 'amy', 'age': 22},{'name': 'joe', 'age': 31},] ,'multiline':"""one
       two
       three""",'string':"my first project"}
    return render(request, 'first_app/home.html',d)
