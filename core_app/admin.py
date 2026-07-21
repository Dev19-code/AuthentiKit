from django.contrib import admin
from .models import DemoVerificationCode

@admin.register(DemoVerificationCode)
class DemoVerificationCodeAdmin(admin.ModelAdmin):
    # أسماء الحقول في الموديل التي ستظهر كأعمدة في الجدول
    list_display = ('code', 'product_name', 'brand')
    
    # أسماء الحقول التي يمكنك البحث من خلالها في لوحة التحكم
    search_fields = ('code', 'product_name', 'brand')