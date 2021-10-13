"""
管理员接口
"""
from db import models


def admin_register_interface(user_name, password):
    """
    管理员注册接口
    :return:
    """
    # 1、判断用户是否存在
    # 调用Admin中的，select方法，由该方法调用db_handler中的select_data功能获取对象
    admin_obj = models.Admin.select(user_name)
    #   若存在不允许用户注册，返回用户已存在视图
    if admin_obj:
        return False, '用户已存在！'
    #   若存在则允许用户注册，调用类实例化得到对象并保存
    admin_obj = models.Admin(user_name, password)
    # 对象调用save会将admin_obj传给save方法
    admin_obj.save()

    return True, '注册成功！'


# def admin_login_interface(user_name, password):
#     """
#     管理员登录接口
#     :return:
#     """
#     # 1.判断用户是否存在
#     admin_obj = models.Admin.select(user_name)
#     # 2.若用户不存在，返回给视图层
#     if not admin_obj:
#         return False, '用户名不存在！'
#     # 用户名存在，校验密码
#     else:
#         if password == admin_obj.pwd:
#             return True, '登录成功！'
#         else:
#             return False, '密码错误，登录失败！'


def create_school_interface(school_name, school_addr, admin_name):
    """
    创建学校接口
    :param school_name: 学校名称
    :param school_addr: 学校地址
    :param admin_name: 管理员名称
    :return:
    """
    # 1.查看学校是否存在
    school_obj = models.School.select(school_name)
    # 2.若学校存在返回Fals告诉学校存在
    if school_obj:
        return False, '学校已存在！'
    # 3.若学校不存在，创建学校（由管理员对象创建）
    admin_obj = models.Admin.select(admin_name)  # 获取到当前管理员对象
    admin_obj.create_school(school_name, school_addr)

    return True, f'[{school_name}]学校创建成功'


def admin_create_course_interface(school_name, course_name, admin_name):
    """

    :param school_name:
    :param course_name:
    :param admin_name:
    :return:
    """
    # 1.查看课程是否存在。先获取学校对象中的课程列表，判断当前课程是否存在列表中
    school_obj = models.School.select(school_name)

    # 2.若课程存在返回Flase
    if course_name in school_obj.course_list:
        return False, '当前课程已存在！'
    # 3.若课程不存在则由管理员创建课程
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj, course_name)
    return True, f'[{course_name}]创建成功，绑定给[{school_name}]学校'


def admin_create_teacher_interface(teacher_name, admin_name, teacher_pwd='123'):
    # 1.判断老师是否存在
    teacher_obj = models.Teacher.select(teacher_name)

    # 2.若存在则返回不能创建
    if teacher_obj:
        return False, '老师已存在！'
    # 3.若不存在则让管理员来创建
    admin_obj = models.Admin.select(admin_name)

    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, f'[{teacher_name}]老师创建成功！'
