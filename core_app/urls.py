from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quick-verify/', views.quick_verify_ajax, name='quick_verify'),
]