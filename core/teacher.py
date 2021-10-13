"""
老师视图
"""
from lib import common
from interface import teacher_interface, common_interface
from db import models

teacher_info = {
    'user': None
}


def login():
    """
    -1、登录
    :return:
    """
    while True:
        user_name = input('请输入昵称：').strip()
        user_pwd = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(user_name, user_pwd, user_type='teacher')
        if flag:
            teacher_info['user'] = user_name
            print(msg)
            break
        else:
            print(msg)


@common.auth('teacher')
def check_course():
    """
    -2、查看教授课程
    :return:
    """
    flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
    if course_list:
        print(course_list)
    else:
        print(course_list)


@common.auth('teacher')
def choose_course():
    """
    -3、选择教授课程
    :return:
    """
    while True:
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print(f'编号：{index}  学校名称：{school_name}')
        choice = input('请输入选择学校：')
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print('请输入正确编号')
            continue
        # 获取选择后的学校名字
        school_name = school_list[choice]
        flag, course_list = teacher_interface.check_all_course_interface(school_name)
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}  课程名称：{course_name}')
        choice = input('请输入选择课程：')
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('请输入正确编号')
            continue
        course_name = course_list[choice]
        flag, msg = teacher_interface.add_course_interface(course_name, teacher_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth('teacher')
def check_stu_from_course():
    """
    -4、查看课程下的学生
    :return:
    """
    while True:
        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}  课程名称：{course_name}')
        choice = input('请输入课程编号：')
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('请输入正确编号!')
            continue
        course_name = course_list[choice]
        flag, student_list = teacher_interface.check_course_student_interface(course_name)
        if flag:
            print(student_list)
            break
        else:
            print(student_list)
            break


@common.auth('teacher')
def change_socre():
    """
    -5、修改学生分数
    :return:
    """
    while True:
        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}  课程名称：{course_name}')
        choice = input('请输入课程编号：')
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('请输入正确编号!')
            continue
        course_name = course_list[choice]
        flag, student_list = teacher_interface.check_course_student_interface(course_name)
        if not flag:
            print(student_list)
            break
        for index, course_name in enumerate(student_list):
            print(f'编号：{index}  学生名称：{student_list}')
        choice = input('请输入学生编号：')
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(student_list)):
            print('请输入正确编号!')
            continue
        student_name = student_list[choice]
        course_score = input(f'请输入[{student_name}]的[{course_name}]成绩：')
        if not course_score.isdigit():
            print('请输入数字！')
            continue
        course_score = int(course_score)
        msg = teacher_interface.input_course(student_name, course_name, course_score)
        print(msg)
        break


func_dict = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_socre,
}


def teacher_view():
    while True:
        print('''
        ====欢迎来到老师视图====
        -1、登录
        -2、查看教授课程
        -3、选择教授课程
        -4、查看课程下的学生
        -5、修改学生分数
        =========end=========
        ''')

        choice = input('请输入功能编号：').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue
        func_dict.get(choice)()
