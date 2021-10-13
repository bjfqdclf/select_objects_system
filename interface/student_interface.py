"""
学生接口
"""
from db import models


def register_interface(student_name, student_pwd):
    """
    学生注册接口
    :param student_name:
    :param student_pwd:
    :return:
    """
    student_obj = models.Student.select(student_name)
    if student_obj:
        return False, '该用户名已存在！'
    student_obj = models.Student(student_name, student_pwd)
    student_obj.save()
    return True, f'[{student_name}]用户已创建！'


def choice_school_interface(school_name, student_name):
    """
    选择学校
    :param school_name: 学校名
    :param student_name: 学生名
    :return:
    """
    # 1、判断当前学生是否在学校中
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False, '当前学生已经选择过学校'
    # 2。若不存在学校则调用学生对象中选择学校的方法
    student_obj.choice_school(school_name)
    return True, '选择学校成功'


def get_course_list_interface(student_name):
    """
    获取学生课程列表
    :param student_name: 学生名字
    :return:
    """
    # 获取当前学生对象
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    # 没有选择学校
    if not school_name:
        return False, '没有选择学校，请先选择学校！'
    # 有学校，获取学校对象中的课程列表
    school_obj = models.School.select(school_name)
    # 判断当前学校中是否有课程
    course_list = school_obj.course_list
    if not course_list:
        return False, '没有课程，请联系管理员'
    return True, course_list


def choice_course_interface(course_name, student_name):
    """
    学生选择课程接口
    :param course_name: 课程名
    :param student_name: 学生名
    :return:
    """
    # 判断当前课程是否已经存在
    student_obj = models.Student.select(student_name)
    if course_name in student_obj.course_list:
        return False, '不可以重复选择此课程！'
    # 调用学生对象添加课程方法
    student_obj.add_course(course_name)

    return True, f'[{course_name}]--课程添加成功'


def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    if student_obj.score:
        return student_obj.score
    else:
        return None


def get_student_course_list_interface(student_name):
    """
    获取学生已有课程
    :param student_name: 学生名
    :return:
    """
    student_obj = models.Student.select(student_name)
    if not student_obj.course_list:
        return False, '未学习课程，请添加课程！'
    return True, student_obj.course_list


def pay_course_interface(course_name, course_pay, student_name):
    """
    支付接口
    :param course_name:
    :param course_pay:
    :param student_name:
    :return:
    """
    student_obj = models.Student.select(student_name)
    if student_obj.pay[course_name] != 0:
        return False, '课程已缴费,无需重复缴费！'
    student_obj.pay_course(course_name, course_pay)
    return True, f'[{course_name}]缴费 {course_pay}元'
