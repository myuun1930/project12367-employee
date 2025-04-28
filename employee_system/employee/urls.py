from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # หน้าแสดงรายชื่อพนักงาน
    path('add/', views.add_employee, name='add_employee'),  # หน้าเพิ่มพนักงาน
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),  # หน้าแก้ไขพนักงาน
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),  # ลบพนักงาน
    path('search/', views.search_employee, name='search_employee'),  # หน้าแสดงผลการค้นหา
]