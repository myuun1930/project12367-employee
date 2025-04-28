from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'salary', 'phone_number')  # คอลัมน์ที่แสดงในตาราง
    search_fields = ('first_name', 'last_name', 'position', 'salary')  # ค้นหาตามชื่อ, ตำแหน่ง, เงินเดือน
    list_filter = ('position',)  # ฟิลเตอร์ตามตำแหน่ง
    list_per_page = 20 