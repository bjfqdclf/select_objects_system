"""
老师接口
"""
from db import models
from interface import common_interface


def check_course_interface(teacher_name):
    """
    查看课程
    :param teacher_name:
    :return:
    """
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.course_list
    if not course_list:
        return False, '未添加课程'
    return True, course_list


def check_all_course_interface(school_name):
    """
    查看可选择课程
    :param school_name:
    :return:
    """
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if course_list:
        return True, course_list
    else:
        return False, '当前学校未添加课程，请联系管理员！'


def add_course_interface(course_name, teacher_name):
    """
    添加课程
    :param course_name:
    :param teacher_name:
    :return:
    """
    teacher_obj = models.Teacher.select(teacher_name)
    flag = teacher_obj.add_course(course_name)
    if flag:
        return True, f'[{course_name}]课程添加成功！'
    return False, '不可重复添加该课程！'


def check_course_student_interface(course_name):
    """
    查看课程下的学生
    :param course_name:
    :return:
    """
    course_obj = models.Course.select(course_name)
    student_list = course_obj.student_list
    if student_list:
        return True, student_list
    return False, '该课程下没有学生'


def input_course(student_name, course_name, course_score):
    student_obj = models.Student.select(student_name)
    student_obj.input_course_score(course_name, course_score)
    return '修改成功'
