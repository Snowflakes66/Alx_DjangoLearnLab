from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer

class NotificationView(APIView):
    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user)
        return Response(NotificationSerializer(notifications, many=True).data, status=status.HTTP_200_OK)

