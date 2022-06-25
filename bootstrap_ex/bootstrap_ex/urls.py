from django.contrib import admin
from django.urls import path
import bootapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bootapp.views.home)
]
