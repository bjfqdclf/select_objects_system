"""
用于存放类

学校类、学员类、讲师类、课程类、管理员类
"""
from db import db_handler


class Base:
    # 查看数据
    @classmethod
    def select(cls, user_name):  # Admin,user_name
        obj = db_handler.select_data(cls, user_name)
        return obj

    def save(self):
        # 让db_handler中的save_data保存对象
        db_handler.save_data(self)


class Admin(Base):
    """
    user
    pwd
    """

    # 调用类时候触发
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self, school_name, school_addr):
        """
        该方法内部调用学校类并实例化得到对象保存
        :param school_name:
        :param school_addr:
        :return:
        """
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_course(self, school_obj, course_name):
        """
        创建课程
        :param school_obj: 课程对象
        :param course_name: 课程名
        :return:
        """
        course_obj = Course(course_name)
        course_obj.save()
        school_obj.course_list.append(course_name)
        school_obj.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


class Student(Base):
    def __init__(self, name, password):
        self.user = name
        self.pwd = password
        self.school = None
        self.course_list = []
        self.score = {}  # {'course_name':val}
        self.pay = {}  # {'course_name':False}

    def choice_school(self, school_name):
        """
        学生添加学校
        :param school_name:
        :return:
        """
        self.school = school_name
        self.save()

    def add_course(self, course_name):
        """
        学生添加课程
        :param course_name:
        :return:
        """
        # 学生添加课程
        self.course_list.append(course_name)
        self.pay[course_name] = False
        self.score[course_name] = 0
        self.save()
        # 课程绑定学生
        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()

    def input_course_score(self, course_name, course_score):
        self.score[course_name] = course_score
        self.save()

    def pay_course(self, course_name, course_pay):
        """
        交钱
        :param course_name: 课程名称
        :param course_pay: 所交费用
        :return:
        """
        self.pay[course_name] = course_pay
        self.save()


class Teacher(Base):
    def __init__(self, name, password):
        self.user = name
        self.pwd = password
        self.course_list = []

    def add_course(self, course_name):
        """
        添加课程
        :param course_name:
        :return:
        """
        # 判断老师是否已经添加该课程
        if course_name in self.course_list:
            return False
        self.course_list.append(course_name)
        self.save()
        return True


class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class School(Base):
    def __init__(self, name, addr):
        """
        必须写self.user因为db_handler里面select_data统一规范
        :param name:必须用user
        :param addr:
        """
        self.user = name
        self.addr = addr
        # 每所学校都有相应的课程，课程列表
        self.course_list = []
