from django.shortcuts import render

# Create your views here.

def about(request):
    if request.method == 'POST':
        # print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,"about.html",{'name':name,'email':email,'select':select})
    return render(request,"about.html")

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request,"form.html",{'name':name,'email':email})
    return render(request,"form.html")
