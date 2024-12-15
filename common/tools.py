import datetime
import os
def get_now_time():
    return datetime.datetime.now()

def get_project_path():
    """
    获取项目的绝对路径
    :return:
    """
    """
    ! 不能存在和项目名称一样的文件夹
    """
    # print(__file__) # D:\dasi\test\trading_system_autotest\common\tools.py
    # print(__name__) # __main__
    file_path=os.path.dirname(__file__) # 文件所在的目录
    # print(file_path) # D:\dasi\test\trading_system_autotest\common
    project_name = "trading_system_autotest"
    # print(file_path.find(project_name)) # 找子串第一次出现的位置，find
    # 截取项目所在的位置，即项目之前的绝对路径，D:\dasi\test\
    # print(file_path[:file_path.find(project_name)])
    # 获取项目的绝对路径，D:\dasi\test\trading_system_autotest
    # print(file_path[:file_path.find(project_name)+len(project_name)])
    return file_path[:file_path.find(project_name)+len(project_name)]
"""
获取yaml文件相对项目的相对路径
"""
def sep(path,add_sep_before=False,add_sep_after=False):
    # print(path)
    # print(os.sep)
    # 字符串列表拼接
    all_path = os.sep.join(path)
    # print(all_path)
    if add_sep_before:
        all_path = os.sep +all_path
    if add_sep_after:
        all_path = all_path + os.sep
    # print(all_path)
    return all_path

def get_img_path(img_name):
    """
    获取商品图片的路径
    :param img_name:
    :return:
    """
    img_dir_path = get_project_path()+sep(["img",img_name],add_sep_before=True)
    return img_dir_path


# if __name__ == '__main__':
#     print(get_project_path())
    # print(get_now_time())
    # sep(["config","environment.yaml"],True)
    print(get_img_path("cg.jpg"))