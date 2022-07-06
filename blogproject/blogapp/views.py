import imp
from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'index.html')
    
# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):                   # POST 요청이 들어오면 
        post = Blog()                               # Blog 객체 생성해서
        post.title = request.POST['title']          # title, body, date에 데이터를 담고
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()                                 # database에 저장

    return redirect('home')