from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from .models import Student
from info_manage import models


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
    student = None
    for stu in Student.objects.all():
        student = stu
    return render(request, "stu_information/stu_information.html",
                  {"stu_name": student.stu_name, "stu_id": student.stu_id, "stu_sex": student.stu_sex,
                   "birth_date": student.birth_date, "identity_number": student.identity_number,
                   "native_place": student.native_place, "admission_time": student.admission_time,
                   "home_address": student.home_address, "department_name": student.department_name,
                   "class_name": student.class_name})


@login_required
def score(request):
    """学生个人成绩查询"""
    return render(request, "stu_information/score.html")


@login_required
def award(request):
    """学生获奖记录"""
    return render(request, "stu_information/award_information.html")


@login_required
def add_award_info(request):
    """增加获奖记录"""
    return render(request, "stu_information/add_award_info.html")


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


@login_required
def modify_stu_info(request):
    """修改个人信息页面"""
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        stu_name = request.POST['stu_name']
        stu_sex = request.POST['stu_sex']
        birth_date = request.POST['birth_date']
        identity_number = request.POST['identity_number']
        native_place = request.POST['native_place']
        admission_time = request.POST['admission_time']
        home_address = request.POST['home_address']
        department_name = request.POST['department_name']
        department_object = models.Department.objects.create(department_name=department_name)
        class_name = request.POST['class_name']
        class_object = models.Class.objects.create(class_name=class_name)
        models.Student.objects.create(stu_id=stu_id, stu_name=stu_name, stu_sex=stu_sex, birth_date=birth_date,
                                      identity_number=identity_number, native_place=native_place,
                                      admission_time=admission_time, home_address=home_address,
                                      department_name=department_object, class_name=class_object)

    return render(request, "stu_information/modify_stu_info.html")
