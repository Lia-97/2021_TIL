from django.urls import path
from . import views # 현재 폴더에 있는 views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('ping/', views.ping, name='ping'),
    path('pong/', views.pong, name='pong'),
    path('<int:num>/', views.detail, name='detail'),
]
