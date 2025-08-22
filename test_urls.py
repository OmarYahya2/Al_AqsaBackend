#!/usr/bin/env python
"""
اختبار URLs للتأكد من عمل جميع الروابط
"""
import os
import django
from django.test import Client
from django.urls import reverse

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

def test_urls():
    """اختبار جميع URLs"""
    client = Client()
    
    print("🧪 اختبار URLs لمختبر الأقصى الطبي")
    print("=" * 50)
    
    # اختبار الصفحة الرئيسية (redirect)
    print("🏠 اختبار الصفحة الرئيسية...")
    try:
        response = client.get('/')
        if response.status_code == 302:
            print(f"✅ الصفحة الرئيسية: {response.status_code} - إعادة توجيه إلى {response.url}")
        else:
            print(f"❌ الصفحة الرئيسية: {response.status_code}")
    except Exception as e:
        print(f"❌ خطأ في الصفحة الرئيسية: {e}")
    
    # اختبار Contact API GET
    print("\n📬 اختبار Contact API...")
    try:
        response = client.get('/api/contact/')
        if response.status_code == 200:
            print(f"✅ Contact API GET: {response.status_code}")
        else:
            print(f"❌ Contact API GET: {response.status_code}")
    except Exception as e:
        print(f"❌ خطأ في Contact API: {e}")
    
    # اختبار API Info
    print("\nℹ️ اختبار معلومات API...")
    try:
        response = client.get('/api/info/')
        if response.status_code == 200:
            print(f"✅ API Info: {response.status_code}")
            # عرض جزء من المحتوى
            if hasattr(response, 'json'):
                data = response.json()
                print(f"   📋 المشروع: {data.get('project', 'غير محدد')}")
        else:
            print(f"❌ API Info: {response.status_code}")
    except Exception as e:
        print(f"❌ خطأ في API Info: {e}")
    
    # اختبار Admin (GET فقط للتحقق من الوصول)
    print("\n🔧 اختبار لوحة التحكم...")
    try:
        response = client.get('/admin/')
        if response.status_code in [200, 302]:  # 200 إذا مسجل دخول، 302 إذا يحتاج تسجيل دخول
            print(f"✅ Admin Panel: {response.status_code}")
        else:
            print(f"❌ Admin Panel: {response.status_code}")
    except Exception as e:
        print(f"❌ خطأ في Admin Panel: {e}")
    
    print("\n" + "=" * 50)
    print("✅ انتهى الاختبار")

if __name__ == '__main__':
    test_urls()
