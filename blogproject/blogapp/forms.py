from xml.etree.ElementTree import Comment
from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

# Blog 모델을 기반으로 form 생성
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']