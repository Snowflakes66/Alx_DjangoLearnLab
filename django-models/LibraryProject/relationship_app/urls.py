from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # home page
    path('', views.home_view, name='home'),
    # Built-in login view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # Built-in logout view
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # Custom registration view
    path('register/', views.register, name='register'),
    # List all books
    path('books/', views.list_books, name='list_books'),
    # Library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
]

