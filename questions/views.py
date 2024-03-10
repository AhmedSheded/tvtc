from django.shortcuts import render
from .serializers import CategorySerializer, QuestionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Question
# Create your views here.


class CategoryAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionAPIView(APIView):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        questions = Question.objects.filter(category=category)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






