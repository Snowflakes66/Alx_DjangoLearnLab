
from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView, FeedView
from .import views


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', LikePostView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view()),
    path('feed/', views.FeedView.as_view()),

]
