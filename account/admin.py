from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'email', 'phone', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email', 'subject', 'phone')
    readonly_fields = ('created_at',)
    
    # ترتيب الحقول في صفحة التفاصيل
    fieldsets = (
        ('معلومات المتصل', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('تفاصيل الرسالة', {
            'fields': ('subject', 'message')
        }),
        ('معلومات إضافية', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'الاسم الكامل'
    
    # تخصيص عرض الوقت
    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M')
    created_at.short_description = 'تاريخ الإرسال'
    
    class Meta:
        verbose_name = 'رسالة اتصال'
        verbose_name_plural = 'رسائل الاتصال'
