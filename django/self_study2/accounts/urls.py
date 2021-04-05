from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
