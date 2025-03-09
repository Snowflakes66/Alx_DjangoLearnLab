from django.urls import path
from . import views

urlpatterns = [
    path('example_form/', views.example_form_view, name='example_form'),
]


