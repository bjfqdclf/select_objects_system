"""
学生视图
"""
from lib import common
from interface import student_interface, common_interface

student_info = {
    'user': None
}


def register():
    """
    -1、注册
    :return:
    """
    while True:
        student_name = input('请输入昵称：').strip()
        student_pwd = input('请输入密码：').strip()
        re_student_pwd = input('请再次输入密码：').strip()
        if student_pwd == re_student_pwd:
            flag, msg = student_interface.register_interface(student_name, student_pwd)

            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print('注册失败，两次密码不一致！')


def login():
    """
    -2、登录
    :return:
    """
    while True:
        user_name = input('请输入昵称：').strip()
        user_pwd = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(user_name, user_pwd, user_type='student')
        if flag:
            student_info['user'] = user_name
            print(msg)
            break
        else:
            print(msg)


@common.auth('student')
def choice_school():
    """
    -3、选择校区
    :return:
    """
    while True:
        # 打印所有校区
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print(f'编号：{index}  学校名称：{school_name}')

        # 让学生选择输入学校编号
        choice = input('请输入学校编号：').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print('请输入正确编号')
            continue

        # 获取选择后的学校名字
        school_name = school_list[choice]
        flag, msg = student_interface.choice_school_interface(school_name, student_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth('student')
def choice_course():
    """
    -4、选择课程
    :return:
    """
    while True:
        # 打印学生可以选择的所有课程
        flag, course_list = student_interface.get_course_list_interface(student_info.get('user'))
        if not flag:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}  课程名称：{course_name}')
        choice = input('请输入课程编号：').strip()
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('请输入正确的编号！')
        course_name = course_list[choice]
        flag, msg = student_interface.choice_course_interface(course_name, student_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.auth('student')
def check_socre():
    """
    -5、查看分数
    :return:
    """
    # 直接调用学生分数查看接口
    score = student_interface.check_score_interface(student_info.get('user'))
    if not score:
        print('没有选择课程')
    else:
        print(score)


@common.auth('student')
def pay():
    while True:
        flag, course_list = student_interface.get_student_course_list_interface(student_info.get('user'))
        if not flag:
            print(course_list)
            break
        for inmdex, course_name in enuerate(course_list):
            print(f'编号：{index}  课程名称：{course_name}')
        choice = input('请输入缴费课程编号：').strip()
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('请输入正确的编号！')
        course_name = course_list[choice]
        course_pay = input('请输入缴费金额：')
        if not course_pay.isdigit():
            print('请输入数字！')
            continue
        flag, msg = student_interface.pay_course_interface(course_name, course_pay, student_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


func_dict = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_socre,
    '6': pay
}


def student_view():
    while True:
        print('''
        ====欢迎来到学生视图====
        -1、注册
        -2、登录
        -3、选择校区
        -4、选择课程
        -5、查看分数
        -6、支付学费
        =========end=========
        ''')

        choice = input('请输入功能编号：').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue
        func_dict.get(choice)()
