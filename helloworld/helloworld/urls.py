from django.contrib import admin
from django.urls import path, include
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home), # http://127.0.0.1:8000/ 라는 url로 들어가면 myapp.views.home 실행시켜라!
    path('test/', myapp.views.test),
    path('products/', include('product.urls')), # product/~ 로 나가는 url들은 product/urls.py가 관리할거야!
    path('boards/', include('board.urls'))
]
