from django.urls import path
from .views import CategoryAPIView, QuestionAPIView, ai

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category'),
    path('categories/<int:id>/', QuestionAPIView.as_view(), name='questions'),
    path('ai', ai, name='ai')
]