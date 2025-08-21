from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactMessageSerializer

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # تخزين الرسالة في قاعدة البيانات
            print("Received contact message:", serializer.validated_data)
            return Response(
                {"message": "تم الاستلام! سنرد عليك في أقرب وقت ممكن"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
