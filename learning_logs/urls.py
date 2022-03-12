"""learning_logs의  URL 패턴을 정의합니다"""
from django.urls import URLPattern, path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #홈페이지
    path('',views.index, name='index'),
    path('topics/',views.topics, name='topics'),
    # 단일 주제 페이지
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #새 주제를 추가하는 페이지
    path('new_topic/', views.new_topic, name='new_topic'),
    #새 항목을 추가하는 페이지
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #항목 수정 페이지
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry'),
]