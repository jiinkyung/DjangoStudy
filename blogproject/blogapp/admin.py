from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

admin.site.register(Blog) # admin 사이트에서 확인 가능
admin.site.register(Comment)