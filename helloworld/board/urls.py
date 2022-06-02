from django.urls import path
from board import views

urlpatterns = [
    path('', views.board), # http://127.0.0.1:8000/boards/
    path('first/', views.boardfirst) # http://127.0.0.1:8000/boards/first/
]