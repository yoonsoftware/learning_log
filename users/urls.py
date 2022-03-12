"""users 앱의 URL 패턴을 정의 합니다."""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns =[
    # 기본 인증 URL
    path('',include('django.contrib.auth.urls')),

    # 등록 페이지
    path('register/', views.register, name='register'),
]