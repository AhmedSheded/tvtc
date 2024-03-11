import json
from .gpt import chatgpt
from django.views.decorators.csrf import csrf_exempt
from .serializers import CategorySerializer, QuestionSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import Category, Question
# from .gpt import chatgpt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def ai(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        question = data.get('question', '')
        answer = chatgpt(question)
        return JsonResponse({'answer': answer})
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)


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






