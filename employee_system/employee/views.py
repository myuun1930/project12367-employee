from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q  # เพิ่มการใช้ Q object

# ฟังก์ชันแสดงรายชื่อพนักงาน
def employee_list(request):
    employees = Employee.objects.all()  # ดึงข้อมูลพนักงานทั้งหมด
    return render(request, 'employee_list.html', {'employees': employees})

# ฟังก์ชันเพิ่มพนักงานใหม่
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # กลับไปที่หน้ารายชื่อพนักงาน
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

# ฟังก์ชันแก้ไขพนักงาน
def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # กลับไปที่หน้ารายชื่อพนักงาน
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

# ฟังก์ชันลบพนักงาน
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('employee_list')  # กลับไปที่หน้ารายชื่อพนักงาน

# ฟังก์ชันค้นหาพนักงาน
def search_employee(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')  # รับข้อมูลคำค้นหาจากฟอร์ม
        employees = Employee.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(position__icontains=query) | 
            Q(salary__icontains=query)
        )
        return render(request, 'search_employee.html', {'employees': employees, 'query': query})