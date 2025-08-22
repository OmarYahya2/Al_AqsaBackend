# 🔗 دليل URLs - مختبر الأقصى الطبي Backend

## ✅ تم إضافة الصفحة الرئيسية بنجاح!

### 🏠 الروابط المتاحة:

#### **الصفحة الرئيسية:**
```
GET /
```
- **الوظيفة:** إعادة توجيه تلقائي إلى Django Admin
- **الهدف:** `/admin/`
- **النتيجة:** فتح لوحة التحكم مباشرة ✅

#### **لوحة التحكم:**
```
GET /admin/
```
- **الوظيفة:** Django Admin Panel
- **تسجيل الدخول:** `admin` / `admin123456`
- **المميزات:** تصميم عربي محسن بدون خلفيات بيضاء

#### **API الاتصال:**
```
GET /api/contact/     # اختبار API
POST /api/contact/    # إرسال رسالة
```
- **الوظيفة:** استقبال رسائل نموذج الاتصال
- **مثال POST:**
```json
{
  "first_name": "أحمد",
  "last_name": "محمد",
  "email": "ahmed@example.com",
  "phone": "+970123456789",
  "subject": "استفسار",
  "message": "رسالة اختبار"
}
```

#### **🆕 معلومات API:**
```
GET /api/info/
```
- **الوظيفة:** صفحة معلومات شاملة عن API
- **المحتوى:** 
  - تفاصيل المشروع
  - قائمة بجميع endpoints
  - أمثلة الاستخدام
  - معلومات التواصل

### 🔄 سلوك إعادة التوجيه:

**عند زيارة البكند مباشرة:**

1. **`https://al-aqsabackend-uokt.onrender.com/`**
   → **يعيد التوجيه إلى** `https://al-aqsabackend-uokt.onrender.com/admin/`

2. **`https://al-aqsabackend-uokt.onrender.com/admin/`**
   → **يعرض لوحة التحكم**

3. **`https://al-aqsabackend-uokt.onrender.com/api/contact/`**
   → **يعرض API للاتصال**

4. **`https://al-aqsabackend-uokt.onrender.com/api/info/`**
   → **يعرض معلومات API**

### 📊 جدول الروابط:

| الرابط | الوظيفة | النتيجة |
|--------|---------|----------|
| `/` | الصفحة الرئيسية | ↩️ إعادة توجيه لـ Django Admin |
| `/admin/` | لوحة التحكم | 🏛️ Django Admin |
| `/api/contact/` | API الاتصال | 📬 استقبال/إرسال رسائل |
| `/api/info/` | معلومات API | ℹ️ تفاصيل وتوثيق |

### 🧪 اختبار الروابط:

```bash
# 1. اختبار الصفحة الرئيسية (redirect)
curl -I https://al-aqsabackend-uokt.onrender.com/
# Expected: 302 Found, Location: /admin/

# 2. اختبار معلومات API
curl https://al-aqsabackend-uokt.onrender.com/api/info/
# Expected: JSON مع تفاصيل API

# 3. اختبار Contact API
curl https://al-aqsabackend-uokt.onrender.com/api/contact/
# Expected: رسالة API يعمل

# 4. اختبار Admin (في المتصفح)
# https://al-aqsabackend-uokt.onrender.com/admin/
```

### 🔧 التكوين في الكود:

```python
# Backend/urls.py
urlpatterns = [
    path('', home_view, name='home'),  # الصفحة الرئيسية
    path('admin/', admin.site.urls),   # لوحة التحكم
    path('api/', include('account.urls')),  # APIs
    path('api/info/', APIInfoView.as_view()),  # معلومات API
]

# account/views.py
def home_view(request):
    return redirect('https://al-aqsa-medical-lab.vercel.app')
```

---

## ✅ **لا مزيد من خطأ 404!**

الآن عند زيارة الـ Backend مباشرة:
- 🚫 **لن تظهر صفحة 404**
- ↩️ **سيتم التوجيه تلقائياً للـ Frontend**
- 🎯 **تجربة مستخدم سلسة ومتطورة**

🎉 **جاهز للنشر والاستخدام!**
