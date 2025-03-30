from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import login
from rest_framework.views import APIView
from .models import User
from posts.serializers import PostSerializer
from posts.models import Post




class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

class UserProfileAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    

class FollowUserView(APIView):
    def post(self, request, user_id):
        user_to_follow = User.objects.get(id=user_id)
        request.user.following.add(user_to_follow)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnfollowUserView(APIView):
    def post(self, request, user_id):
        user_to_unfollow = User.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response(status=status.HTTP_204_NO_CONTENT)

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')



# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("""
#         <h1>Social Media API</h1>
#         <p>Available endpoints:</p>
#         <ul>
#             <li><a href="/api/auth/register/">/api/auth/register/</a> - User registration</li>
#             <li><a href="/api/auth/login/">/api/auth/login/</a> - User login</li>
#             <li><a href="/admin/">/admin/</a> - Admin interface</li>
#         </ul>
#     """)