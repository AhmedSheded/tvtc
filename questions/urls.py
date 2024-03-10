from django.urls import path
from .views import CategoryAPIView, QuestionAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category'),
    path('categories/<int:id>/', QuestionAPIView.as_view(), name='questions')
]