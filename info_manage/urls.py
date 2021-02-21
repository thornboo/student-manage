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
    # 系统设置选项
    path('settings/', views.sys_settings, name="settings"),

    # 个人信息栏
    # 1、学生个人信息
    path('stu_information/', views.stu_information, name='stu_information'),
    # 2、个人成绩查询
    path('score/', views.score, name="score"),
    # 3、个人获奖记录
    path('award/', views.award, name="award"),
    # 4、处分记录
    path('punish/', views.punish, name="punish"),
    # 修改个人信息
    path('modify/', views.modify_stu_info, name="modify_stu_info"),
    # 增加获奖记录
    path('add_award_info/', views.add_award_info, name="add_award_info"),

    # 学籍管理栏
    # 1、个人学籍查询
    path('school_register/', views.school_roll, name="school_register"),
    # 2、学信网查询学籍
    # 3、查看家庭成员
    path('member/', views.fam_member, name="memebr"),
    # 4、学籍变动信息
    path('roll_change/', views.school_roll_change, name="roll_change"),

    # 考试管理栏
    path('exam_information/', views.exam_information, name="exam_information"),
    # 1、考试信息
    path('exam_info/', views.exam_information, name="exam_info"),
    # 2、考试排名
    path('score_inquire/', views.score_inquire, name="score_inquire"),

    # 财务管理栏
    # 1、学费查询
    path('tuition/', views.tuition, name="tuition"),
    # 2、IC卡充值查询
    path('recharge/', views.card_recharge, name="recharge"),

    # 通知管理栏
    # 1、通讯录
    # 2、收件箱
    # 3、发件箱
    # 4、草稿箱
]
