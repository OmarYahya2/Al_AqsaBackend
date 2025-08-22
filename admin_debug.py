#!/usr/bin/env python
"""
اختبار وتشخيص مشاكل Django Admin
"""
import os
import django

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
import logging

def debug_admin():
    print("🔍 تشخيص مشاكل Django Admin")
    print("=" * 50)
    
    # فحص المستخدمين
    print("👥 فحص المستخدمين:")
    users = User.objects.filter(is_superuser=True)
    if users:
        for user in users:
            print(f"✅ Admin User: {user.username} (Active: {user.is_active})")
    else:
        print("❌ لا يوجد مستخدم admin")
    
    # فحص URLs
    print("\n🔗 فحص URLs:")
    try:
        admin_url = reverse('admin:index')
        print(f"✅ Admin URL: {admin_url}")
    except Exception as e:
        print(f"❌ خطأ في Admin URL: {e}")
    
    # فحص Static Files
    print("\n📂 فحص Static Files:")
    print(f"📍 STATIC_URL: {settings.STATIC_URL}")
    print(f"📍 STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"📍 STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    
    # فحص Admin Static Files
    admin_css_path = settings.STATIC_ROOT / 'admin' / 'css' / 'base.css'
    if admin_css_path.exists():
        print(f"✅ Admin CSS موجود: {admin_css_path}")
    else:
        print(f"❌ Admin CSS غير موجود: {admin_css_path}")
    
    # فحص WhiteNoise
    print(f"\n🔧 إعدادات WhiteNoise:")
    if hasattr(settings, 'STATICFILES_STORAGE'):
        print(f"✅ STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
    
    middlewares = settings.MIDDLEWARE
    has_whitenoise = any('whitenoise' in m.lower() for m in middlewares)
    if has_whitenoise:
        print("✅ WhiteNoise middleware مفعل")
    else:
        print("❌ WhiteNoise middleware غير مفعل")
    
    # فحص ALLOWED_HOSTS
    print(f"\n🌐 إعدادات الأمان:")
    print(f"🔐 DEBUG: {settings.DEBUG}")
    print(f"🌐 ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    # اختبار تشغيل Admin
    print(f"\n🧪 اختبار Admin:")
    try:
        from django.contrib import admin
        print(f"✅ Django Admin مستورد بنجاح")
        print(f"📊 عدد النماذج المسجلة: {len(admin.site._registry)}")
    except Exception as e:
        print(f"❌ خطأ في Django Admin: {e}")

if __name__ == '__main__':
    debug_admin()
