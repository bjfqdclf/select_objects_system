"""
保存对象和获取数据
"""
import os
from conf import setting
import pickle


# 保存数据
def save_data(obj):
    # 1.获取对象保存文件夹路径
    # 以类名当作文件夹的名字
    class_name = obj.__class__.__name__  # 获取当前对象的类的名字
    user_dir_path = os.path.join(
        setting.DB_PATH, class_name
    )
    # 2.判断文件夹是否存在，不存在创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3.拼接当前用户pickle文件路径，以用户做文件名
    user_path = os.path.join(
        user_dir_path, obj.user  # 当前用户的名字
    )
    # 4.打开文件保存对象,通过pickle处理
    with open(user_path, 'wb')as f:
        pickle.dump(obj, f)


# 查看数据
def select_data(cls, user_name):  # 类，user
    class_name = cls.__name__  # 获取当前类的名字
    user_dir_path = os.path.join(
        setting.DB_PATH, class_name
    )
    # 2.判断文件夹是否存在，不存在创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3.拼接当前用户pickle文件路径，以用户做文件名
    user_path = os.path.join(
        user_dir_path, user_name  # 当前用户的名字
    )
    # 4.判断文件如果存在并返回，若不存在
    if os.path.exists(user_path):
        # 4.打开文件获取对象
        with open(user_path, 'rb')as f:
            obj = pickle.load(f)
            return obj
    return None
