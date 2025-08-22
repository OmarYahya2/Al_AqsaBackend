from django.db import models

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=100, verbose_name="اسم العائلة")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف")
    subject = models.CharField(max_length=200, verbose_name="الموضوع")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
    
    class Meta:
        verbose_name = "رسالة اتصال"
        verbose_name_plural = "رسائل الاتصال"
        ordering = ['-created_at']
