#!/usr/bin/env python
"""
فحص إعدادات الملفات الثابتة للتأكد من عملها
"""
import os
import django
from django.conf import settings

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

def check_static_settings():
    print("🔍 فحص إعدادات الملفات الثابتة:")
    print(f"📂 STATIC_URL: {settings.STATIC_URL}")
    print(f"📂 STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"📂 STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    
    if hasattr(settings, 'STATICFILES_STORAGE'):
        print(f"🗜️ STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
    
    # التحقق من وجود ملفات CSS
    css_file = settings.STATIC_ROOT / 'css' / 'admin_custom.css'
    if css_file.exists():
        print(f"✅ ملف CSS موجود: {css_file}")
    else:
        print(f"❌ ملف CSS غير موجود: {css_file}")
    
    # التحقق من ملفات Django admin
    admin_css = settings.STATIC_ROOT / 'admin' / 'css' / 'base.css'
    if admin_css.exists():
        print(f"✅ ملفات Django admin موجودة: {admin_css}")
    else:
        print(f"❌ ملفات Django admin غير موجودة: {admin_css}")
    
    # التحقق من middleware
    middlewares = settings.MIDDLEWARE
    has_whitenoise = any('whitenoise' in m.lower() for m in middlewares)
    if has_whitenoise:
        print("✅ WhiteNoise middleware مفعل")
    else:
        print("❌ WhiteNoise middleware غير مفعل")

    print("\n📋 إعدادات الأمان:")
    print(f"🔐 DEBUG: {settings.DEBUG}")
    print(f"🌐 ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    print("\n📋 إعدادات CORS:")
    if hasattr(settings, 'CORS_ALLOWED_ORIGINS'):
        print(f"🔗 CORS_ALLOWED_ORIGINS: {settings.CORS_ALLOWED_ORIGINS}")

if __name__ == '__main__':
    check_static_settings()
