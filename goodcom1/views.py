from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)

def index(request):
	#return HttpResponse("안녕하세요 goodcom1에 오신것을 환영합니다.")
    return render(request,'goodcom1/semantic.html')
def menu1(request):
	#return HttpResponse("안녕하세요 goodcom1에 오신것을 환영합니다.")
    return render(request,'goodcom1/menu1.html')

# Create your views here.
