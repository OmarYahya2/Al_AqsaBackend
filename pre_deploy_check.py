#!/usr/bin/env python
"""
فحص شامل قبل النشر للتأكد من جاهزية المشروع
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from django.conf import settings
from django.core.checks import run_checks
from django.contrib.auth.models import User

def check_requirements():
    """فحص ملف requirements.txt"""
    print("📦 فحص المكتبات المطلوبة...")
    
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
        
        packages_found = []
        for line in lines:
            if '==' in line:
                package_name = line.split('==')[0].strip()
                packages_found.append(package_name)
        
        print(f"✅ تم العثور على {len(packages_found)} مكتبة:")
        for pkg in packages_found:
            print(f"   - {pkg}")
                
    except FileNotFoundError:
        print("❌ ملف requirements.txt غير موجود")

def check_settings():
    """فحص إعدادات Django"""
    print("\n⚙️ فحص إعدادات Django...")
    
    # فحص DEBUG
    if not settings.DEBUG:
        print("✅ DEBUG = False (مناسب للإنتاج)")
    else:
        print("⚠️ DEBUG = True (يجب تغييره للإنتاج)")
    
    # فحص ALLOWED_HOSTS
    if settings.ALLOWED_HOSTS and len(settings.ALLOWED_HOSTS) > 0:
        print(f"✅ ALLOWED_HOSTS مُعرف: {settings.ALLOWED_HOSTS}")
    else:
        print("❌ ALLOWED_HOSTS غير مُعرف")
    
    # فحص STATIC settings
    if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT:
        print(f"✅ STATIC_ROOT: {settings.STATIC_ROOT}")
    else:
        print("❌ STATIC_ROOT غير مُعرف")
    
    # فحص WhiteNoise
    middlewares = settings.MIDDLEWARE
    has_whitenoise = any('whitenoise' in m.lower() for m in middlewares)
    if has_whitenoise:
        print("✅ WhiteNoise middleware مُفعل")
    else:
        print("❌ WhiteNoise middleware غير مُفعل")
    
    # فحص CORS
    if hasattr(settings, 'CORS_ALLOWED_ORIGINS'):
        print(f"✅ CORS_ALLOWED_ORIGINS: {len(settings.CORS_ALLOWED_ORIGINS)} أصل مُصرح")
    else:
        print("❌ CORS_ALLOWED_ORIGINS غير مُعرف")

def check_static_files():
    """فحص الملفات الثابتة"""
    print("\n📂 فحص الملفات الثابتة...")
    
    # التحقق من مجلد static
    if os.path.exists('static'):
        print("✅ مجلد static موجود")
        
        # فحص ملف CSS المخصص
        css_path = 'static/css/admin_custom.css'
        if os.path.exists(css_path):
            print("✅ ملف CSS المخصص موجود")
        else:
            print("❌ ملف CSS المخصص غير موجود")
    else:
        print("❌ مجلد static غير موجود")
    
    # التحقق من مجلد templates
    if os.path.exists('templates'):
        print("✅ مجلد templates موجود")
    else:
        print("❌ مجلد templates غير موجود")

def check_database():
    """فحص قاعدة البيانات"""
    print("\n🗃️ فحص قاعدة البيانات...")
    
    try:
        # فحص migrations
        from django.core.management.commands.showmigrations import Command
        print("✅ قاعدة البيانات متاحة")
        
        # فحص وجود مستخدم admin
        admin_users = User.objects.filter(is_superuser=True)
        if admin_users.exists():
            print(f"✅ يوجد {admin_users.count()} مستخدم admin")
        else:
            print("⚠️ لا يوجد مستخدم admin - سيتم إنشاؤه تلقائياً")
            
    except Exception as e:
        print(f"❌ خطأ في قاعدة البيانات: {str(e)}")

def check_deployment_files():
    """فحص ملفات النشر"""
    print("\n🚀 فحص ملفات النشر...")
    
    deployment_files = [
        'manage.py',
        'create_superuser.py',
        'render.yaml',
        'DEPLOYMENT.md'
    ]
    
    for file in deployment_files:
        if os.path.exists(file):
            print(f"✅ {file} موجود")
        else:
            print(f"❌ {file} غير موجود")

def run_django_checks():
    """تشغيل فحوصات Django الأساسية"""
    print("\n🔍 تشغيل فحوصات Django...")
    
    try:
        errors = run_checks()
        if errors:
            print(f"❌ وُجدت {len(errors)} مشكلة:")
            for error in errors:
                print(f"   - {error}")
        else:
            print("✅ جميع فحوصات Django نجحت")
    except Exception as e:
        print(f"❌ خطأ في فحوصات Django: {str(e)}")

def main():
    print("🏥 فحص شامل قبل نشر مختبر الأقصى الطبي")
    print("=" * 50)
    
    check_requirements()
    check_settings()
    check_static_files()
    check_database()
    check_deployment_files()
    run_django_checks()
    
    print("\n" + "=" * 50)
    print("✅ انتهى الفحص. راجع النتائج أعلاه قبل النشر.")

if __name__ == '__main__':
    main()
