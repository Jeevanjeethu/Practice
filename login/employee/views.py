from django.shortcuts import render, redirect, HttpResponse
from django.http import *
from employee.forms import EmployeeForm
from employee.models import Employee
from django.db.models import Q
from django.contrib import messages, auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def fun(request):
    return render(request,'home.html')
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
def login(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'login.html',{'form':form})
def logout(request):
    return render(request,'logout.html')
def redir(reqquest):
    return redirect('/emp')
    return render(request,'index.html',{'form':form})
def redir3(reqquest):
    return redirect('/show')
    # return render(request,'index.html',{'form':form})
def redir2(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'menu.html',{'form':form})
def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def show1(request):
    employees = Employee.objects.all()
    return render(request,"show1.html",{'employees':employees})
def show2(request):
    employees = Employee.objects.all()
    return render(request,"show2.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
def search(request):
    if request.method== 'POST':
        srch = request.POST["srh"]
        if srch:
             match  = Employee.objects.filter(Q(eid__icontains=srch)|
                                              Q(ename__icontains=srch))
             if match:
                 return render(request,'search.html',{'sr':match})
             else:
                 messages.error(request,'no results found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')
