from django.contrib import admin
from .models import Pet


#Tạo giao diện nhà quản trị để thao tác với model dữ liệu đã import

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
     list_display = ['name', 'species', 'breed', 'age', 'sex']