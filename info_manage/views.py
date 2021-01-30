from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
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
def stu_information(request):
    """学生个人信息"""
    stu_id = request.GET.get("姓名")
    return render(request, 'info_manage/stu_information.html', stu_id)


@login_required
def school_register(request):
    """学生学籍管理"""
    return render(request, 'info_manage/school_register.html')


@login_required
def department(request):
    """院系管理"""
    return render(request, 'info_manage/department.html')


@login_required
def Class(request):
    """班级管理"""
    return render(request, 'info_manage/class.html')


@login_required
def exam_information(request):
    """学校考试管理"""
    return render(request, 'info_manage/exam_information.html')


@login_required
def tuition(request):
    """学费管理"""
    return render(request, 'info_manage/tuition_inquiry.html')
