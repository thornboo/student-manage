from django.contrib import admin
from .models import *


# 院系信息
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'department_id',
        'department_name',
    ]
    search_fields = ('department_id', 'department_name')


# 班级信息
class ClassAdmin(admin.ModelAdmin):
    list_display = [
        'class_id',
        'class_name',
    ]
    search_fields = ('class_id', 'class_name')


# 学生个人信息
class StuAdmin(admin.ModelAdmin):
    # 设置列表可显示的字段
    list_display = [
        'stu_id',
        'stu_name',
        'stu_sex',
        'class_name',
        'department_name',
        'birth_date',
        'identity_number',
        'native_place',
        'admission_time',
        'home_address',
    ]
    # 设置查找字段
    search_fields = ('stu_id', 'stu_name')
    # 设置过滤字段
    list_filter = ('stu_sex', 'class_name', 'department_name', 'birth_date', 'identity_number', 'native_place',
                   'admission_time', 'home_address')


# 学籍变更记录
class SchoolRegisterAdmin(admin.ModelAdmin):
    list_display = [
        'status',
        'stu_id',
        'description',
    ]
    search_list = ('stu_id',)
    list_filter = ('status', 'description')


# 获奖记录
class AwardAdmin(admin.ModelAdmin):
    list_display = [
        'stu_id',
        'awaerd_name',
        'awaerd_date',
        'grade',
        'description',
    ]
    search_fields = ('stu_id',)
    list_filter = ('awaerd_name', 'awaerd_date', 'grade', 'description')


# 处分记录
class PunishAdmin(admin.ModelAdmin):
    list_display = [
        'stu_id',
        'punish_name',
        'punish_date',
        'degree',
        'description',
    ]
    search_fields = ('stu_id',)
    list_filter = ('punish_name', 'punish_date', 'degree', 'description')


# 成绩查询
class ScoreAdmin(admin.ModelAdmin):
    list_display = [
        'serial_number',
        'semester',
        'exam_subject',
        'exam_categories',
        'exam_time',
        'exam_scores',
        'description',
    ]
    search_fields = ('semester',)
    list_filter = ('serial_number', 'exam_subject', 'exam_categories', 'exam_time', 'exam_scores', 'description')


# 家庭成员信息
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'member_name',
        'member_age',
        'member_identity',
        'member_employer',
        'description',
    ]
    search_fields = ('member_name',)
    list_filter = ('member_age', 'member_identity', 'member_employer', 'description')


# 考试信息查询
class ExamAdmin(admin.ModelAdmin):
    list_display = [
        'exam_name',
        'exam_date',
        'exam_place',
        'description',
    ]
    search_fields = ('exam_date',)
    list_filter = ('exam_name', 'exam_place', 'description')


# 学费查询
class TuitionAdmin(admin.ModelAdmin):
    list_display = [
        'semester',
        'status',
        'payment_method',
        'cost',
    ]
    search_fields = ('semester',)
    list_filter = ('status', 'payment_method', 'cost')


class EventAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """为应用程序的功能排序"""
        ordering = {
            "Student": 1,
            "Class": 2,
            "Department": 3,
            "SchoolRegister": 4,
            "AwardInformation": 5,
            "PunishInformation": 6,
        }
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])
        return app_list


admin.site.register(Student, StuAdmin)  # 学生个人信息
admin.site.register(Department, DepartmentAdmin)  # 院系信息
admin.site.register(Class, ClassAdmin)  # 班级信息
admin.site.register(AwardInformation, AwardAdmin)  # 获奖记录
admin.site.register(SchoolRegister, SchoolRegisterAdmin)  # 学籍变更记录
admin.site.register(PunishInformation, PunishAdmin)  # 处分记录
admin.site.register(ScoreInquire, ScoreAdmin)  # 成绩查询
admin.site.register(FamilyMember, MemberAdmin)  # 家庭成员信息
admin.site.register(ExamInfomation, ExamAdmin)  # 考试信息查询
admin.site.register(TuitionInquiry, TuitionAdmin)  # 学费管理
admin.AdminSite.site_header = "学生信息管理系统"
admin.AdminSite.site_title = "管理"
