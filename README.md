# 🏥 مختبر الأقصى الطبي - Backend

الواجهة الخلفية لموقع مختبر الأقصى الطبي مبنية باستخدام Django و Django REST Framework.

## 🌟 المميزات

- ✅ API لنموذج الاتصال مع معالجة شاملة للأخطاء
- ✅ لوحة تحكم Django محسنة مع تصميم عربي
- ✅ دعم CORS للتكامل مع Frontend
- ✅ نموذج بيانات محسن للرسائل
- ✅ إعدادات إنتاج جاهزة للنشر
- ✅ دعم اللغة العربية وتنسيق RTL
- ✅ ملفات CSS مخصصة لتحسين المظهر

## 📁 هيكل المشروع

```
Al_AqsaBackend/
├── Backend/           # إعدادات Django الرئيسية
│   ├── settings.py    # إعدادات محسنة مع CORS
│   ├── urls.py        # توجيهات URL
│   └── wsgi.py        # WSGI للنشر
├── account/           # تطبيق إدارة الرسائل
│   ├── models.py      # نموذج ContactMessage
│   ├── views.py       # API views مع error handling
│   ├── serializers.py # Django REST serializers
│   ├── admin.py       # إعدادات admin محسنة
│   └── urls.py        # توجيهات API
├── static/            # ملفات CSS مخصصة
├── templates/         # قوالب HTML محسنة
├── requirements.txt   # المكتبات المطلوبة
└── DEPLOYMENT.md      # دليل النشر الشامل
```

## 🚀 التثبيت والإعداد

### 1. تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### 2. إعداد قاعدة البيانات

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. جمع الملفات الثابتة

```bash
python manage.py collectstatic --noinput
```

### 4. إنشاء مستخدم admin

```bash
python create_superuser.py
```

أو يدوياً:

```bash
python manage.py createsuperuser
```

### 5. تشغيل الخادم

```bash
python manage.py runserver
```

الموقع سيكون متاحاً على: `http://localhost:8000`

## 🔗 نقاط API

### 📬 Contact API

**إرسال رسالة اتصال:**
```
POST /api/contact/
Content-Type: application/json

{
  "first_name": "أحمد",
  "last_name": "محمد", 
  "email": "ahmed@example.com",
  "phone": "+970123456789",
  "subject": "استفسار عن الخدمات",
  "message": "مرحبا، أريد الاستفسار عن خدماتكم"
}
```

**استجابة ناجحة:**
```json
{
  "success": true,
  "message": "تم الاستلام! سنرد عليك في أقرب وقت ممكن",
  "data": {
    "id": 1,
    "first_name": "أحمد",
    "last_name": "محمد",
    "email": "ahmed@example.com"
  }
}
```

**اختبار الـ API:**
```
GET /api/contact/
```

### 🔧 لوحة التحكم

```
GET /admin/
```

**معلومات تسجيل الدخول الافتراضية:**
- Username: `admin`
- Password: `admin123456`

## 🌐 النشر

### على Render

راجع ملف `DEPLOYMENT.md` للحصول على تعليمات مفصلة.

**خطوات سريعة:**

1. رفع الكود إلى GitHub
2. إنشاء Web Service على Render
3. إضافة متغيرات البيئة:
   ```
   DJANGO_SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app.onrender.com
   ```
4. نشر الخدمة

## ⚙️ التكوين

### إعدادات CORS

```python
CORS_ALLOWED_ORIGINS = [
    "https://al-aqsa-medical-lab.vercel.app",  # Frontend URL
    "http://localhost:3000",  # التطوير المحلي
]
```

### إعدادات قاعدة البيانات

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### إعدادات الملفات الثابتة

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

## 🎨 التصميم والواجهة

- **CSS مخصص:** ملفات CSS محسنة لـ Django admin
- **قوالب عربية:** دعم كامل للغة العربية
- **تصميم متجاوب:** يعمل على جميع الأجهزة
- **ألوان محسنة:** تدرجات وظلال احترافية

## 🧪 الاختبار

### اختبار محلي

```bash
# تشغيل خادم التطوير
python manage.py runserver

# اختبار API
curl -X POST http://localhost:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{"first_name":"أحمد","last_name":"محمد","email":"test@example.com","subject":"اختبار","message":"رسالة اختبار"}'
```

### اختبار الإنتاج

```bash
# اختبار API المنشور
curl https://al-aqsabackend-uokt.onrender.com/api/contact/
```

## 🔒 الأمان

- **Secret Key:** مخفي في متغيرات البيئة
- **Debug Mode:** مغلق في الإنتاج
- **CORS:** محدود للمواقع المصرح بها
- **CSRF Protection:** فعال للحماية

## 📊 المراقبة والصيانة

### مراقبة الأخطاء

- راجع logs في لوحة تحكم Render
- استخدم Django admin لمراقبة الرسائل
- تحقق من صحة API endpoints

### النسخ الاحتياطي

```bash
# نسخ احتياطي لقاعدة البيانات
python manage.py dumpdata > backup.json

# استرداد النسخة الاحتياطية
python manage.py loaddata backup.json
```

## 🆘 استكشاف الأخطاء

### مشاكل شائعة:

1. **CORS Errors:**
   - تحقق من `CORS_ALLOWED_ORIGINS`
   - تأكد من ترتيب middleware

2. **Static Files لا تظهر:**
   - شغل `collectstatic`
   - تحقق من `STATIC_ROOT`

3. **Database Errors:**
   - شغل `migrate`
   - تحقق من الصلاحيات

## 📈 التطوير المستقبلي

- [ ] ترقية إلى PostgreSQL
- [ ] إضافة authentication system
- [ ] إضافة API للحجوزات
- [ ] إضافة نظام إشعارات
- [ ] إضافة تقارير إحصائية

## 🤝 المساهمة

للمساهمة في المشروع:

1. Fork المشروع
2. إنشاء branch جديد
3. إجراء التغييرات
4. إرسال Pull Request

## 📄 الترخيص

هذا المشروع مرخص تحت [MIT License](LICENSE).

## 📞 التواصل

- **البريد الإلكتروني:** info@alaqsamedical.com
- **الهاتف:** +970 123 456 789
- **الموقع:** https://al-aqsa-medical-lab.vercel.app

---

**تم التطوير بـ ❤️ لخدمة مختبر الأقصى الطبي**

