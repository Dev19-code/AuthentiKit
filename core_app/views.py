from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'core_app/home.html')


def quick_verify_ajax(request):
    """
    نقطة نهاية AJAX للتحقق السريع من كود المنتج.
    TODO: لما زميلك يخلّص store_app.models.AuthenticityCode،
    هنستبدل القاموس ده باستعلام حقيقي:
        from store_app.models import AuthenticityCode
        record = AuthenticityCode.objects.filter(code=code).first()
    """
    code = request.GET.get('code', '').strip().upper()

    # بيانات وهمية مؤقتة للتجربة فقط
    fake_db = {
        'AK-1001': 'Original Samsung Fast Charger',
        'AK-2050': 'Original iPhone Lightning Cable',
    }

    if code in fake_db:
        return JsonResponse({
            'status': 'authentic',
            'product_name': fake_db[code],
        })
    return JsonResponse({'status': 'not_found'})