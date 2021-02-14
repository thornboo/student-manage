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


@login_required
def modify_stu_info(request):
    """修改个人信息页面"""
    # 从前端获取数据
    #     stu_id = request.POST.get("stu_id")
    #     stu_name = request.POST.get("stu_name")
    #     stu_sex = request.POST.get("stu_sex")
    #     birth_date = request.POST.get("birth_date")
    #     identity_number = request.POST.get("identity_number")
    #     native_place = request.POST.get("native_place")
    #     admission_time = request.POST.get("admission_time")
    #     home_address = request.POST.get("home_address")
    #     department_name = request.POST.get("department_name")
    #     class_name = request.POST.get("class_name")
    #     # 写入数据库
    #     stu = Student()  # 初始化数据库
    #     stu.id = stu_id
    #     stu.name = stu_name
    #     stu.sex = stu_sex
    #     stu.birth = birth_date
    #     stu.identity = identity_number
    #     stu.native = native_place
    #     stu.admission = admission_time
    #     stu.address = home_address
    #     stu.department = department_name
    #     stu.sch_class = class_name
    #     stu.save()
    #     result = "success"
    # return render(request, "stu_information/modify_stu_info.html")
    print(request.POST)
    return render(request, "stu_information/modify_stu_info.html")
