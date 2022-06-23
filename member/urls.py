from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1/join 요청시 member앱의 views
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('logout/', views.logout, name='logout'),
]