# تعليمات نشر مختبر الأقصى الطبي - Backend

## 📋 نظرة عامة

هذا الدليل يوضح كيفية نشر الواجهة الخلفية (Backend) لموقع مختبر الأقصى الطبي على منصة Render.

## 🚀 المتطلبات

- حساب على [Render.com](https://render.com)
- حساب GitHub مع repository للمشروع
- Python 3.11+
- Django 5.2+

## 📁 هيكل المشروع

```
Al_AqsaBackend/
├── Backend/           # إعدادات Django الرئيسية
├── account/          # تطبيق إدارة الرسائل والحسابات
├── static/           # الملفات الثابتة (CSS, JS, Images)
├── staticfiles/      # الملفات المجمعة للإنتاج
├── templates/        # قوالب HTML
├── db.sqlite3        # قاعدة البيانات (للتطوير فقط)
├── manage.py         # أداة إدارة Django
├── requirements.txt  # المكتبات المطلوبة
└── create_superuser.py # إنشاء مستخدم admin
```

## ⚙️ إعدادات الإنتاج

### 1. متغيرات البيئة المطلوبة

يجب إضافة هذه المتغيرات في إعدادات Render:

```bash
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com,localhost,127.0.0.1
```

### 2. تحديث settings.py للإنتاج

```python
import os

# أمان
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-key')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# قاعدة البيانات (يمكن ترقيتها إلى PostgreSQL لاحقاً)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CORS للسماح بالاتصال من Frontend
CORS_ALLOWED_ORIGINS = [
    "https://al-aqsa-medical-lab.vercel.app",
    "http://localhost:3000",
]
```

## 🔧 خطوات النشر على Render

### الخطوة 1: رفع الكود إلى GitHub

```bash
git add .
git commit -m "Deploy backend with CORS and styling fixes"
git push origin main
```

### الخطوة 2: إنشاء Web Service على Render

1. سجل دخولك إلى [Render Dashboard](https://dashboard.render.com)
2. انقر على "New" → "Web Service"
3. اربط حساب GitHub واختر repository المشروع
4. اختر المجلد: `Al_AqsaBackend`
5. املأ البيانات كالتالي:

**إعدادات الخدمة:**
- **Name**: `al-aqsa-backend` (أو أي اسم تختاره)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command**: `gunicorn Backend.wsgi:application`

### الخطوة 3: إضافة متغيرات البيئة

في قسم "Environment Variables" أضف:

```
DJANGO_SECRET_KEY = your-generated-secret-key
DEBUG = False
ALLOWED_HOSTS = your-app-name.onrender.com,localhost,127.0.0.1
```

### الخطوة 4: النشر

1. انقر على "Create Web Service"
2. انتظر حتى انتهاء البناء والنشر
3. ستحصل على URL مثل: `https://your-app-name.onrender.com`

## 🔒 إنشاء مستخدم Admin

بعد النشر الناجح، قم بتشغيل:

```bash
# على Render Console أو محلياً قبل النشر
python create_superuser.py
```

**معلومات تسجيل الدخول:**
- Username: `admin`
- Password: `admin123456`
- Email: `admin@alaqsamedical.com`

**رابط لوحة التحكم:** `https://your-app-name.onrender.com/admin/`

## 🌐 ربط Frontend مع Backend

تأكد من تحديث الروابط في Frontend (Next.js) لتشير إلى Backend المنشور:

```javascript
// في ContactForm.jsx
const res = await fetch(
  "https://your-app-name.onrender.com/api/contact/",
  {
    method: "POST",
    headers: { 
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(data),
  }
);
```

## 🧪 اختبار الـ API

### اختبار GET

```bash
curl https://your-app-name.onrender.com/api/contact/
```

### اختبار POST

```bash
curl -X POST https://your-app-name.onrender.com/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "أحمد",
    "last_name": "محمد",
    "email": "ahmed@example.com",
    "phone": "+970123456789",
    "subject": "استفسار",
    "message": "مرحبا، أريد الاستفسار عن خدماتكم"
  }'
```

## 📊 مراقبة الأداء

### لوقات الأخطاء
يمكنك مراقبة الأخطاء من خلال:
1. Render Dashboard → Logs
2. Django admin panel → View logs

### التحقق من الصحة
- `GET /api/contact/` - يجب أن يعيد رسالة نجاح
- `POST /api/contact/` - يجب أن يحفظ الرسالة في قاعدة البيانات
- `/admin/` - يجب أن تظهر لوحة التحكم مع التصميم المحسن

## 🔄 تحديثات مستقبلية

### للتحديث:
1. ادفع التغييرات إلى GitHub
2. Render سيقوم بإعادة النشر تلقائياً
3. تأكد من عمل migrations: `python manage.py migrate`

### ترقية قاعدة البيانات:
يُنصح بالترقية إلى PostgreSQL للإنتاج:

```python
# في requirements.txt
psycopg2-binary==2.9.7

# في settings.py
import dj_database_url
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

## 🆘 استكشاف الأخطاء

### مشاكل شائعة:

1. **CORS Errors:**
   - تأكد من إضافة Frontend URL في `CORS_ALLOWED_ORIGINS`
   - تحقق من ترتيب middleware

2. **Static Files لا تظهر:**
   - تأكد من تشغيل `collectstatic`
   - تحقق من إعدادات `STATIC_ROOT`

3. **Database Errors:**
   - تأكد من تشغيل migrations
   - تحقق من صلاحيات الملفات

4. **500 Internal Server Error:**
   - راجع logs في Render Dashboard
   - تأكد من صحة متغيرات البيئة

## 📞 الدعم

للحصول على المساعدة:
- راجع [Render Documentation](https://render.com/docs)
- تحقق من [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

## 🎯 ملخص سريع

```bash
# 1. تحضير المشروع
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python create_superuser.py

# 2. النشر على Render
# - ربط GitHub repository
# - إضافة متغيرات البيئة
# - نشر الخدمة

# 3. اختبار
curl https://your-app-name.onrender.com/api/contact/
```

✅ **تم الانتهاء من إعداد Backend بنجاح!**
