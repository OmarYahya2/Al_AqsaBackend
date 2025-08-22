#!/usr/bin/env python
"""
إنشاء مستخدم admin للوصول إلى لوحة التحكم
"""
import os
import django

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    username = 'admin'
    email = 'admin@alaqsamedical.com'
    password = 'admin123456'
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f'تم إنشاء مستخدم المدير: {username}')
        print(f'كلمة المرور: {password}')
        print('يمكنك الوصول إلى لوحة التحكم عبر: /admin/')
    else:
        print('مستخدم المدير موجود بالفعل')

if __name__ == '__main__':
    create_superuser()
