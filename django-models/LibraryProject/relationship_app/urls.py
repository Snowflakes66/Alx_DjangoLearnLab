from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books

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
        # Admin view URL
    path('admin_view/', views.admin_view, name='admin_view'),

    # Librarian view URL
    path('librarian_view/', views.librarian_view, name='librarian_view'),

    # Member view URL
    path('member_view/', views.member_view, name='member_view'),

    path('add/', views.add_book, name='add_book'),

    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]

