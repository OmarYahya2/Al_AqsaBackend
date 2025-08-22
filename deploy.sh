#!/bin/bash

# Django deployment script for Render
echo "🚀 بدء عملية النشر لمختبر الأقصى الطبي"

# Install dependencies
echo "📦 تثبيت المكتبات المطلوبة..."
pip install -r requirements.txt

# Collect static files with WhiteNoise
echo "📂 جمع الملفات الثابتة..."
python manage.py collectstatic --noinput

# Run database migrations
echo "🗃️ تطبيق migrations..."
python manage.py migrate

# Create superuser (if doesn't exist)
echo "👤 إنشاء مستخدم admin..."
python create_superuser.py

echo "✅ تم الانتهاء من عملية النشر بنجاح!"

# Start the application with Gunicorn
echo "🌐 بدء تشغيل الخادم..."
exec gunicorn Backend.wsgi:application
