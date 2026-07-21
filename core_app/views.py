from django.shortcuts import render
from django.http import JsonResponse
from .models import DemoVerificationCode

def home(request):
    """
    عرض الصفحة الرئيسية ومعالجة طلبات التحقق عبر Form العادية (POST)
    """
    verification_result = None
    searched_code = ""

    if request.method == "POST":
        searched_code = request.POST.get("product_code", "").strip()
        
        if searched_code:
            demo_item = DemoVerificationCode.objects.filter(code__iexact=searched_code).first()
            if demo_item:
                verification_result = {
                    "status": "valid",
                    "product_name": demo_item.product_name,
                    "brand": demo_item.brand or "غير محدد",
                    "message": "المنتج أصلي ومسجل!"
                }
            else:
                verification_result = {
                    "status": "invalid",
                    "message": "كود التحقق غير صحيح أو غير موجود."
                }

    context = {
        "searched_code": searched_code,
        "verification_result": verification_result,
    }
    return render(request, "core_app/home.html", context)


def quick_verify_ajax(request):
    """
    دالة معالجة طلبات التحقق السريع عبر AJAX
    """
    code_query = request.GET.get('code', '').strip()
    
    if not code_query:
        return JsonResponse({'status': 'empty', 'message': 'يرجى إدخال كود التحقق'})

    demo_item = DemoVerificationCode.objects.filter(code__iexact=code_query).first()
    
    if demo_item:
        return JsonResponse({
            'status': 'valid',
            'product_name': demo_item.product_name,
            'brand': demo_item.brand or 'غير محدد',
            'message': 'المنتج أصلي ومسجل!'
        })
    else:
        return JsonResponse({
            'status': 'invalid',
            'message': 'كود التحقق غير صحيح أو غير موجود.'
        })