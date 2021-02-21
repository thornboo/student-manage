from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    """学校院系信息"""
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=10, verbose_name="全称")

    class Meta:
        db_table = "Department"
        verbose_name = "院系"
        verbose_name_plural = "院系信息"

    def __str__(self):
        return self.department_name


class Class(models.Model):
    """学校班级信息"""
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=10, verbose_name="全称")

    class Meta:
        db_table = "Class"
        verbose_name = "班级"
        verbose_name_plural = "班级信息"

    def __str__(self):
        return self.class_name


class Student(models.Model):
    """学生个人信息"""
    stu_id = models.CharField(max_length=10, verbose_name="学号", primary_key=True)
    stu_name = models.CharField(max_length=10, verbose_name="姓名")
    sex_choice = (('M', '男'), ('W', '女'))
    stu_sex = models.CharField(max_length=4, choices=sex_choice, verbose_name="性别")
    birth_date = models.CharField(verbose_name='出生日期', max_length=10)
    identity_number = models.CharField(max_length=18, verbose_name='身份证号')
    native_place = models.CharField(max_length=50, verbose_name="籍贯")
    admission_time = models.CharField(verbose_name='入学时间', max_length=10)
    home_address = models.CharField(max_length=50, verbose_name='家庭住址')
    department_name = models.ForeignKey(Department, verbose_name="院系", on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, verbose_name="班级", on_delete=models.CASCADE)

    class Meta:
        db_table = "Student"
        verbose_name = "学生"
        verbose_name_plural = "学生个人信息"

    def __str__(self):
        return self.stu_name


class SchoolRegister(models.Model):
    """关于学籍变动的信息"""
    stu_id = models.ForeignKey(Student, verbose_name="学号", on_delete=models.CASCADE)
    change_choice = (('YES', '变动'), ('NO', '无变动'))
    status = models.CharField(max_length=4, choices=change_choice, verbose_name="状态")
    if change_choice == 'YES':
        change_number = models.IntegerField(verbose_name="序号")
        change_path = models.CharField(max_length=50, verbose_name="具体变动信息")
    description = models.CharField(max_length=20, verbose_name="备注")

    class Meta:
        db_table = "SchoolRegister"
        verbose_name = "学籍"
        verbose_name_plural = "学籍变动"

    def __str__(self):
        return self.description


class AwardInformation(models.Model):
    """关于学生获奖情况"""
    stu_id = models.ForeignKey(Student, verbose_name="学号", on_delete=models.CASCADE)
    awaerd_name = models.CharField(max_length=20, verbose_name="奖项名称")
    awaerd_date = models.DateField(verbose_name="获奖时间")
    grade = models.BooleanField(verbose_name="级别", primary_key=True)
    description = models.CharField(max_length=20, verbose_name="备注")

    class Meta:
        db_table = "AwardInformation"
        verbose_name = "获奖"
        verbose_name_plural = "获奖信息"

    def __str__(self):
        return self.description


class PunishInformation(models.Model):
    """关于学生受处分情况"""
    stu_id = models.ForeignKey(Student, verbose_name="学号", on_delete=models.CASCADE)
    punish_name = models.CharField(max_length=10, verbose_name="处分名称")
    punish_date = models.DateField(verbose_name="处分时间")
    degree = models.BooleanField(verbose_name="级别")
    description = models.CharField(max_length=10, verbose_name="备注")

    class Meta:
        db_table = "PunishInformation"
        verbose_name = "处分"
        verbose_name_plural = "处分信息"

    def __str__(self):
        return self.description


class ScoreInquire(models.Model):
    """学生考试及其得分信息"""
    serial_number = models.IntegerField(verbose_name="序号")
    semester = models.CharField(max_length=10, verbose_name="学期")
    exam_subject = models.CharField(max_length=10, verbose_name="考试科目")
    exam_categories = models.CharField(max_length=10, verbose_name="考试类别")
    exam_time = models.DateField(verbose_name="考试时间")
    exam_scores = models.FloatField(verbose_name="考试成绩")
    description = models.CharField(max_length=20, verbose_name="备注")

    class Meta:
        db_table = "ScoreInquire"
        verbose_name = "成绩"
        verbose_name_plural = "成绩查询"

    def __str__(self):
        return self.description


class FamilyMember(models.Model):
    """关于家庭成员的信息"""
    member_name = models.CharField(max_length=5, verbose_name="成员姓名")
    member_age = models.IntegerField(verbose_name="成员年龄")
    member_identity = models.CharField(max_length=5, verbose_name="与本人关系")
    member_employer = models.CharField(max_length=20, verbose_name="成员工作单位")
    description = models.CharField(max_length=20, verbose_name="备注")

    class Meta:
        db_table = "FamilyMember"
        verbose_name = "信息"
        verbose_name_plural = "家庭成员信息"

    def __str__(self):
        return self.description


class ExamInfomation(models.Model):
    """关于学校的考试信息"""
    exam_name = models.CharField(max_length=10, verbose_name="考试名称")
    exam_date = models.DateField(verbose_name="考试时间")
    exam_place = models.CharField(max_length=10, verbose_name="考试地点")
    description = models.CharField(max_length=20, verbose_name="备注")

    class Meta:
        db_table = "ExamInfomation"
        verbose_name = "考试"
        verbose_name_plural = "考试信息查询"

    def __str__(self):
        return self.description


class TuitionInquiry(models.Model):
    """关于学费查询"""
    semester = models.CharField(max_length=10, verbose_name="学期")
    status = models.CharField(max_length=5, verbose_name="是否已缴费")
    payment_choice = (('Alipay', '支付宝'), ('cash', '现金'), ('WeChat', '微信'))
    payment_method = models.CharField(max_length=6, choices=payment_choice, verbose_name="支付方式")
    cost = models.IntegerField(verbose_name="费用")

    class Meta:
        db_table = "TuitionInquiry"
        verbose_name = "学费"
        verbose_name_plural = "学费管理"

    def __str__(self):
        return self.semester
