"""定义info_manage的URL模式"""
from django.urls import path
from . import views

app_name = 'info_manage'

urlpatterns = [
    # 系统主页
    path('', views.index, name='index'),
    # 校园公告
    path('bulletin/', views.bulletin, name='bulletin'),
    # 系统帮助
    path('help/', views.help, name='help'),
    # 学生个人信息
    path('stu_information/', views.stu_information, name='stu_information'),
    # 学籍管理
    path('school_register/', views.school_register, name="school_register"),
    # 考试管理
    path('exam_information/', views.exam_information, name="exam_information"),
    # 财务管理
    path('tuition/', views.tuition, name="tuition"),
    # 通知管理
    # 获奖管理
    # 处分管理
]
