from django.urls import path
from django.http import HttpResponse
from . import views

def signin_placeholder(request):
    return HttpResponse("صفحة تسجيل الدخول - لسه قيد الإنشاء (accounts_app)")

urlpatterns = [
    path('', views.home, name='home'),
    path('quick-verify/', views.quick_verify_ajax, name='quick_verify'),
    path('signin/', signin_placeholder, name='signin'),  # 🔧 مؤقت لحد ما يخلص زميلك
]