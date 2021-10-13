"""
公共接口
"""
import os
from conf import setting
from db import models


def get_all_school_interface():
    """
    获取所有学校
    :return:
    """
    school_dir = os.path.join(
        setting.DB_PATH, 'school'
    )
    # 判断文件夹是否存在
    if not os.path.exists(school_dir):
        return False, '没有学校，请先联系管理员'
    # 文件夹若存在，获取文件夹所有文件名字
    school_list = os.listdir(school_dir)
    return True, school_list


# 公共登录接口
def login_interface(user, pwd, user_type):
    if user_type == 'admin':
        obj = models.Admin.select(user)
    elif user_type == 'student':
        obj = models.Student.select(user)
    elif user_type == 'teacher':
        obj = models.Teacher.select(user)
    else:
        return False, '登录角色不对，请输入角色'

    if not obj:
        return False, '该用户不存在！'
    if obj.pwd == pwd:
        return True, '登陆成功！'
    else:
        return False, '登录失败！'
