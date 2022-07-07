from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 추가

    def __str__(self):
        return self.title