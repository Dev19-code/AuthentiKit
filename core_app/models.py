from django.db import models

class DemoVerificationCode(models.Model):
    """
    موديل مؤقت خاص بـ core_app بس، لتشغيل خاصية التحقق السريع
    في الصفحة الرئيسية. لما store_app يبني AuthenticityCode
    الحقيقي، ممكن الفريق يستبدل الاعتماد على الموديل ده بيه.
    """
    code = models.CharField(max_length=20, unique=True)
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.code} - {self.product_name}"