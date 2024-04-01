from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


class KeyView(APIView):
    parser_classes = [JSONParser]
    
    @csrf_exempt
    def post(self, request):
        uid = request.data['uid']
        key = Key.objects.filter(uid=uid)
        if not key.exists():
            return Response({'response': 'Đã hết hạn sử dụng hoặc chưa cập nhật, vui lòng liên hệ admin'}, status=status.HTTP_404_NOT_FOUND)
        key = key.first()
        if key.time_remaining <= 0:
            return Response({'response': 'Đã hết hạn sử dụng, vui lòng liên hệ admin'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'response': 'Xác thực thành công'}, status=status.HTTP_200_OK)
    def get(self, request):
        return Response({'response': 'MADE BY TRAN MINH LONG'}, status=status.HTTP_200_OK)
    
class UpdateCheck(APIView):
    parser_classes = [JSONParser]
    @csrf_exempt
    def post(self, request):
        version = request.data['version']
        update = Updated.objects.all()
        if not update.exists():
            return Response({'response': False}, status=status.HTTP_200_OK)
        
        # Get the latest update
        update = update.first()
        if update.version > version:
            return Response({'response': True, 
                             'message': 'Đã có bản cập nhật mới', 
                             'url': update.url}, status=status.HTTP_200_OK)
        return Response({'response': False}, status=status.HTTP_200_OK)
    def get(self, request):
        return Response({'response': 'MADE BY TRAN MINH LONG'}, status=status.HTTP_200_OK)

