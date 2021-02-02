from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from .models import Student


@login_required
def index(request):
    """管理系统的主页"""
    return render(request, 'info_manage/index.html')


@login_required
def bulletin(request):
    """系统公告"""
    return render(request, 'info_manage/bulletin.html')


@login_required
def help(request):
    """关于系统的帮助"""
    return render(request, 'info_manage/help.html')


@login_required
def sys_settings(request):
    """学生系统的自定义设置"""
    return render(request, 'info_manage/system_settings.html')


@login_required
def stu_information(request):
    """学生个人信息"""
    return render(request, "stu_information/stu_information.html")


@login_required
def score(request):
    """学生个人成绩查询"""
    return render(request, "stu_information/score.html")


@login_required
def award(request):
    """学生获奖记录"""
    return render(request, "stu_information/award_information.html")


@login_required
def punish(request):
    """学生处分记录查询"""
    return render(request, "stu_information/punish_information.html")


@login_required
def fam_member(request):
    """家庭成员信息查看"""
    return render(request, "school_register/family_member.html")


@login_required
def school_roll(request):
    """学生个人学籍信息查看"""
    return render(request, "school_register/school_roll_info.html")


@login_required
def school_roll_change(request):
    """学生学籍变动信息"""
    return render(request, "school_register/school_roll_change.html")


@login_required
def exam_information(request):
    """学校考试信息查询"""
    return render(request, "exam/exam_information.html")


@login_required
def score_inquire(request):
    """学生考试排名查看"""
    return render(request, "exam/score_inquire.html")


@login_required
def tuition(request):
    """学费查询"""
    return render(request, 'financial/tuition_inquiry.html')


@login_required
def card_recharge(request):
    """IC卡充值"""
    return render(request, "financial/card_recharge.html")
