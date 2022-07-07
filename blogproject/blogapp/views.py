import imp
from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

def home(request):
    # 블로그 글을 모두 띄우는 코드 (DB의 블로그 객체들을 모두 가져옴)
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date') # 내가 가져오고자 하는 정보를 필터링 해서 가져옴 / order_by: 정렬
    return render(request, 'index.html', {'posts' : posts})
    
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

# django form을 이용해서 입력값을 받는 함수
# GET 요청 (= 입력값을 받을 수 있는 html 갖다줘야함.)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용 처리)
# 둘 다 처리가 가능한 함수

def formcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            # 유효한 값이 입력되면 저장
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html 갖다주기
        form = BlogForm()

    # render의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있는데, 이 때 딕셔너리 자료형으로 넘겨줘야함.
    return render(request, 'form_create.html', {'form' :form})

def modelformcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html 갖다주기
        form = BlogModelForm()

    # render의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있는데, 이 때 딕셔너리 자료형으로 넘겨줘야함.
    return render(request, 'form_create.html', {'form' :form})
