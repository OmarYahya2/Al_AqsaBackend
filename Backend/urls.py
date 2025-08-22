from django.contrib import admin
from django.urls import path, include
from account.views import home_view, APIInfoView

urlpatterns = [
    path('', home_view, name='home'),  # الصفحة الرئيسية - إعادة توجيه لـ Django Admin
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('api/info/', APIInfoView.as_view(), name='api_info'),  # معلومات API
]
