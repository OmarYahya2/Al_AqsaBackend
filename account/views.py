from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ContactMessageSerializer
import logging

logger = logging.getLogger(__name__)

class ContactMessageView(APIView):
    permission_classes = [AllowAny]  # السماح لجميع المستخدمين بإرسال رسائل
    
    def post(self, request):
        try:
            logger.info(f"Received contact form data: {request.data}")
            
            serializer = ContactMessageSerializer(data=request.data)
            if serializer.is_valid():
                contact_message = serializer.save()  # تخزين الرسالة في قاعدة البيانات
                logger.info(f"Contact message saved successfully: {contact_message.id}")
                
                return Response(
                    {
                        "success": True,
                        "message": "تم الاستلام! سنرد عليك في أقرب وقت ممكن",
                        "data": {
                            "id": contact_message.id,
                            "first_name": contact_message.first_name,
                            "last_name": contact_message.last_name,
                            "email": contact_message.email
                        }
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                logger.error(f"Validation errors: {serializer.errors}")
                return Response(
                    {
                        "success": False,
                        "message": "خطأ في البيانات المدخلة",
                        "errors": serializer.errors
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except Exception as e:
            logger.error(f"Error processing contact form: {str(e)}")
            return Response(
                {
                    "success": False,
                    "message": "خطأ في الخادم. يرجى المحاولة مرة أخرى لاحقاً",
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def get(self, request):
        """إضافة طريقة GET للاختبار"""
        return Response(
            {
                "success": True,
                "message": "Contact API is working!",
                "endpoint": "POST /api/contact/"
            },
            status=status.HTTP_200_OK
        )
